import requests
from filters import get_adzuna_filter
from config import ADZUNA_APP_ID, ADZUNA_APP_KEY, DATE_FILTER, ADZUNA_LOCATION

def scrape_adzuna(keyword):
    print(f"Scraping Adzuna: '{keyword}' [{DATE_FILTER}]...")

    jobs        = []
    date_filter = get_adzuna_filter(DATE_FILTER)

    for page in range(1, 4):
        url    = f"https://api.adzuna.com/v1/api/jobs/us/search/{page}"
        params = {
            "app_id":           ADZUNA_APP_ID,
            "app_key":          ADZUNA_APP_KEY,
            "what":             keyword,
            "results_per_page": 50,
            "content-type":     "application/json"
        }

        if ADZUNA_LOCATION:
            params["where"] = ADZUNA_LOCATION

        if date_filter:
            params["max_days_old"] = date_filter

        try:
            response = requests.get(url, params=params, timeout=10)
            data     = response.json()
            results  = data.get("results", [])

            if not results:
                break

            for job in results:
                jobs.append({
                    "title":    job.get("title", ""),
                    "company":  job.get("company",  {}).get("display_name", ""),
                    "location": job.get("location", {}).get("display_name", ""),
                    "link":     job.get("redirect_url", ""),
                    "source":   "adzuna",
                    "keyword":  keyword,
                })

            print(f"  Page {page}: found {len(results)} jobs")

        except Exception as e:
            print(f"  Adzuna error: {e}")
            break

    print(f"Adzuna done: {len(jobs)} jobs found")
    return jobs