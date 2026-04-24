import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from filters import get_linkedin_filter
from config import MAX_PAGES, DATE_FILTER

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver

def scrape_linkedin(keyword, location):
    print(f"Scraping LinkedIn: '{keyword}' in '{location}' [{DATE_FILTER}]...")
    driver      = get_driver()
    jobs        = []
    time_filter = get_linkedin_filter(DATE_FILTER)

    try:
        for page in range(MAX_PAGES):
            start = page * 25
            url   = (
                f"https://www.linkedin.com/jobs/search/"
                f"?keywords={keyword.replace(' ', '%20')}"
                f"&location={location.replace(' ', '%20')}"
                f"&start={start}"
            )
            if time_filter:
                url += f"&f_TPR={time_filter}"

            driver.get(url)
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            cards = driver.find_elements(By.CSS_SELECTOR, "div.base-card")

            if not cards:
                print(f"  No more results on page {page + 1}")
                break

            for card in cards:
                try:
                    title   = card.find_element(By.CSS_SELECTOR, "h3.base-search-card__title").text.strip()
                    company = card.find_element(By.CSS_SELECTOR, "h4.base-search-card__subtitle").text.strip()
                    loc     = card.find_element(By.CSS_SELECTOR, "span.job-search-card__location").text.strip()
                    link    = card.find_element(By.CSS_SELECTOR, "a.base-card__full-link").get_attribute("href")

                    if title:
                        jobs.append({
                            "title":    title,
                            "company":  company,
                            "location": loc,
                            "link":     link,
                            "source":   "linkedin",
                            "keyword":  keyword,
                        })
                except Exception:
                    continue

            print(f"  Page {page + 1}: found {len(cards)} cards")
            time.sleep(2)

    finally:
        driver.quit()

    print(f"LinkedIn done: {len(jobs)} jobs found")
    return jobs