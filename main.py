from database import init_db, save_jobs
from display import show_new_jobs
from scrapers.linkedin import scrape_linkedin
from scrapers.adzuna import scrape_adzuna
from config import KEYWORDS, LINKEDIN_LOCATION

def run_scraper():
    print("=" * 60)
    print("  JOB SCRAPER STARTING")
    print(f"  Keywords: {KEYWORDS}")
    print("=" * 60 + "\n")

    init_db()
    all_jobs = []

    for keyword in KEYWORDS:
        linkedin_jobs = scrape_linkedin(keyword, LINKEDIN_LOCATION)
        adzuna_jobs   = scrape_adzuna(keyword)
        all_jobs.extend(linkedin_jobs)
        all_jobs.extend(adzuna_jobs)

    save_jobs(all_jobs)
    show_new_jobs()

if __name__ == "__main__":
    run_scraper()