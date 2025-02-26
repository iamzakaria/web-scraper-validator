# validator.py
def validate_jobs(jobs):
    results = {"passed": [], "failed": []}
    for job in jobs:
        issues = []
        if job["title"] == "N/A":
            issues.append("Missing title")
        if job["company"] == "N/A":
            issues.append("Missing company")
        # Optional: Category-specific rule
        if job["category"] == "qa" and "QA" not in job["title"] and "Quality" not in job["title"]:
            issues.append("Title doesn’t match QA category")
        if issues:
            results["failed"].append({"job": job, "issues": issues})
        else:
            results["passed"].append(job)
    return results

if __name__ == "__main__":
    from scraper import scrape_jobs
    jobs = scrape_jobs(["remote-dev", "qa"])
    results = validate_jobs(jobs)
    print(f"Passed: {len(results['passed'])}")
    print(f"Failed: {len(results['failed'])}")
    if results["failed"]:
        print("Failed jobs:", results["failed"])
    else:
        print("All jobs passed validation!")