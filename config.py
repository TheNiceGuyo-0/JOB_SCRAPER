import os
from dotenv import load_dotenv

load_dotenv()

KEYWORDS = ["Python Developer"]

LINKEDIN_LOCATION = "Remote"
ADZUNA_LOCATION   = ""        # empty = search all US

MAX_PAGES   = 2
DB_NAME     = "jobs.db"
DATE_FILTER = "24h" # options: "24h", "3d", "7d", "any"

ADZUNA_APP_ID  = os.getenv("ADZUNA_APP_ID")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY")