import sqlite3
from config import DB_NAME

def init_db():
    conn   = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            title      TEXT,
            company    TEXT,
            location   TEXT,
            link       TEXT UNIQUE,
            source     TEXT,
            keyword    TEXT,
            date_found TEXT DEFAULT (DATE('now')),
            seen       INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
    print("Database ready!")

def save_jobs(jobs):
    conn      = sqlite3.connect(DB_NAME)
    cursor    = conn.cursor()
    new_jobs_count = 0
    duplicate_jobs_count = 0

    for job in jobs:
        # First, check for duplicates based on title, company, and location
        cursor.execute("SELECT id FROM jobs WHERE title = ? AND company = ? AND location = ?",
                       (job["title"], job["company"], job["location"]))
        if cursor.fetchone():
            duplicate_jobs_count += 1
            continue

        try:
            cursor.execute("""
                INSERT INTO jobs (title, company, location, link, source, keyword)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (job["title"], job["company"], job["location"],
                  job["link"],  job["source"],  job["keyword"]))
            new_jobs_count += 1
        except sqlite3.IntegrityError:
            # This catches duplicates based on the UNIQUE constraint on the 'link' column
            duplicate_jobs_count += 1

    conn.commit()
    conn.close()
    if new_jobs_count == 0:
        print("NO NEW JOBS FOUND")
    else:
        print(f"Saved {new_jobs_count} new jobs to database")

    if duplicate_jobs_count > 0:
        print(f"Skipped {duplicate_jobs_count} duplicate jobs.")

    return new_jobs_count

def get_new_jobs():
    conn   = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, company, location, source, keyword, link, date_found
        FROM jobs
        WHERE seen = 0
        ORDER BY date_found DESC
    """)
    jobs = cursor.fetchall()
    conn.close()
    return jobs

def mark_as_seen(job_ids):
    conn   = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    for job_id in job_ids:
        cursor.execute("UPDATE jobs SET seen = 1 WHERE id = ?", (job_id,))
    conn.commit()
    conn.close()