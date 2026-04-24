# Multi-Source Job Scraper

A Python-based web scraping tool that automatically collects job postings from multiple sources like LinkedIn, Indeed, and Adzuna. It saves new jobs to a local SQLite database and ensures you only see new listings on each run.

## Features

- **Multiple Sources**: Scrapes from LinkedIn and Indeed (using Selenium) and Adzuna (via API).
- **Configurable Search**: Easily change keywords, location, and date filters in `config.py`.
- **Duplicate Prevention**: Uses a local SQLite database with a `UNIQUE` constraint on job links to prevent duplicate entries.
- **"Seen" Tracking**: Remembers which jobs you've already been shown and only displays new ones.
- **Secure API Key Storage**: Manages Adzuna API keys safely using a `.env` file.

---

## Setup and Installation

Follow these steps to get the scraper running on your local machine.

#### 1. Clone the Repository
```bash
git clone https://github.com/TheNiceGuyo-0/JOB_SCRAPER.git
cd JOB_SCRAPER
```

#### 2. Install Dependencies
It's recommended to use a virtual environment. Once your environment is active, install the required packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

#### 3. Set Up Environment Variables
Create a file named `.env` in the root of the project directory. This will store your secret API keys. Get your keys from the Adzuna Developer Portal.

Your `.env` file should look like this:

```dotenv
ADZUNA_APP_ID="YOUR_ADZUNA_APP_ID"
ADZUNA_APP_KEY="YOUR_ADZUNA_APP_KEY"
```

---

## How to Use

1.  **Configure Your Search**: Open `config.py` and modify the following variables to match your needs:
    - `KEYWORDS`: A list of job titles you are searching for (e.g., `["Python Developer", "Data Analyst"]`).
    - `LINKEDIN_LOCATION`: The location to search on LinkedIn (e.g., `"Remote"`, `"New York"`).
    - `DATE_FILTER`: The time window for job postings. Options are `"1h"`, `"24h"`, `"3d"`, `"7d"`, or `"any"`.

2.  **Run the Scraper**: Execute the `main.py` script from your terminal.

    ```bash
    python main.py
    ```

The script will scrape all configured sources, save any new jobs to the `jobs.db` database, and print the new findings to the console.

---

## Project Structure

```
job_scraper/
├── .env                # Stores secret API keys (not committed to Git)
├── .gitignore          # Specifies files for Git to ignore
├── config.py           # Main configuration for search terms, filters, etc.
├── database.py         # Handles all SQLite database interactions
├── display.py          # Formats and prints new job listings to the console
├── filters.py          # Helper functions for generating time filter parameters
├── main.py             # The main entry point to run the entire application
├── README.md           # You are here!
├── requirements.txt    # List of Python package dependencies
└── scrapers/
    ├── adzuna.py       # Scraper for the Adzuna API
    ├── indeed.py       # Scraper for Indeed.com
    └── linkedin.py     # Scraper for LinkedIn.com
```
