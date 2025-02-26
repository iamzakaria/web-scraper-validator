from flask import Flask, render_template
from scraper import scrape_jobs
from validator import validate_jobs
from database import init_db, save_results

app = Flask(__name__)

@app.route('/')
def dashboard():
    init_db()
    jobs = scrape_jobs("https://remoteok.com/remote-dev-jobs")
    results = validate_jobs(jobs)
    save_results(results)
    return render_template("index.html", passed=results["passed"], failed=results["failed"])

if __name__ == "__main__":
    app.run(debug=True)