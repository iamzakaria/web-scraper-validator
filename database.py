import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("results.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS scrape_results
                 (id INTEGER PRIMARY KEY, timestamp TEXT, title TEXT, company TEXT, category TEXT, status TEXT, issues TEXT)''')
    conn.commit()
    conn.close()

def save_results(results):
    conn = sqlite3.connect("results.db")
    c = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for job in results["passed"]:
        c.execute("INSERT INTO scrape_results (timestamp, title, company, category, status) VALUES (?, ?, ?, ?, ?)",
                  (timestamp, job["title"], job["company"], job["category"], "Passed"))
    for item in results["failed"]:
        job = item["job"]
        issues = ", ".join(item["issues"])
        c.execute("INSERT INTO scrape_results (timestamp, title, company, category, status, issues) VALUES (?, ?, ?, ?, ?, ?)",
                  (timestamp, job["title"], job["company"], job["category"], "Failed", issues))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    from scraper import scrape_jobs
    from validator import validate_jobs
    jobs = scrape_jobs(["remote-dev", "qa"])
    results = validate_jobs(jobs)
    save_results(results)
    print("Saved RemoteOK results to results.db")