from database import get_new_jobs, mark_as_seen

def show_new_jobs():
    jobs = get_new_jobs()

    if not jobs:
        print("\n  No new jobs since last check!")
        return

    print(f"\n{'='*60}")
    print(f"  {len(jobs)} NEW JOBS FOUND")
    print(f"{'='*60}\n")

    ids_to_mark = []

    for job in jobs:
        job_id, title, company, location, source, keyword, link, date = job
        print(f"  [{source.upper()}]  {title}")
        print(f"  Company:  {company}")
        print(f"  Location: {location}")
        print(f"  Keyword:  {keyword}")
        print(f"  Found:    {date}")
        print(f"  Link:     {link}")
        print(f"  {'-'*55}")
        ids_to_mark.append(job_id)

    mark_as_seen(ids_to_mark)
    print(f"\n  Marked {len(ids_to_mark)} jobs as seen.")