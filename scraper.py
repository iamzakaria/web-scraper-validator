# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_jobs(search_terms=["remote-dev", "qa"], base_url="https://remoteok.com/"):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    all_jobs = []
    for term in search_terms:
        url = f"{base_url}{term}-jobs"
        response = requests.get(url, headers=headers)
        print(f"Scraping {url} - Status Code: {response.status_code}")
        soup = BeautifulSoup(response.text, "html.parser")
        for job in soup.select("tr.job")[:5]:  # Top 5 per term
            title = job.find("h2", itemprop="title")
            company = job.find("h3", itemprop="name")
            title_text = title.text.strip() if title else "N/A"
            company_text = company.text.strip() if company else "N/A"
            all_jobs.append({"title": title_text, "company": company_text, "category": term})
        print(f"Found {len(soup.select('tr.job')[:5])} jobs for {term}")
    return all_jobs

if __name__ == "__main__":
    jobs = scrape_jobs(["remote-dev", "qa"])
    print(jobs)