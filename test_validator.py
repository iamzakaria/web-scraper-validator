# test_validator.py
from validator import validate_jobs

def test_valid_dev_job():
    jobs = [{"title": "Senior Backend Golang Engineer", "company": "Hippo Technologies", "category": "remote-dev"}]
    results = validate_jobs(jobs)
    assert len(results["passed"]) == 1
    assert len(results["failed"]) == 0

def test_valid_qa_job():
    jobs = [{"title": "QA Engineer", "company": "TestCo", "category": "qa"}]
    results = validate_jobs(jobs)
    assert len(results["passed"]) == 1
    assert len(results["failed"]) == 0

def test_missing_title():
    jobs = [{"title": "N/A", "company": "Hippo Technologies", "category": "remote-dev"}]
    results = validate_jobs(jobs)
    assert len(results["passed"]) == 0
    assert len(results["failed"]) == 1
    assert "Missing title" in results["failed"][0]["issues"]

def test_qa_category_mismatch():
    jobs = [{"title": "Web Developer", "company": "DevCo", "category": "qa"}]
    results = validate_jobs(jobs)
    assert len(results["passed"]) == 0
    assert len(results["failed"]) == 1
    assert "Title doesn’t match QA category" in results["failed"][0]["issues"]