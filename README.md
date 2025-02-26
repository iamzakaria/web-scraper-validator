# RemoteOK Scraper Validator

## Summary
A Python-based SQA tool that scrapes remote developer and QA jobs from RemoteOK, validates their quality, and displays results in a Flask dashboard. Logs data to SQLite, includes pytest tests, and showcases automation—perfect for QA engineers flexing their coding chops.

## Overview
This project automates scraping job listings from `remoteok.com/remote-dev-jobs` (dev roles) and `remoteok.com/qa-jobs` (QA roles), checks for missing titles or companies, and serves the results in a clean web UI. It’s built with a modular design—scraper, validator, database, and dashboard—plus unit tests to ensure reliability. Ideal for SQA portfolios, it demonstrates web scraping, data validation, and reporting skills.

## Features
- **Scraping**: Pulls top 5 jobs each for "remote-dev" and "qa" from RemoteOK.
- **Validation**: Flags jobs with missing titles or companies (optional QA-specific title check available).
- **Database**: Stores results in SQLite with timestamps and categories.
- **Dashboard**: Flask UI showing passed/failed jobs with titles, companies, and categories.
- **Testing**: pytest suite validates the validator logic for both dev and QA jobs.

## Tech Stack
- **Python 3.12: Core language.
- **requests & BeautifulSoup**: Scraping RemoteOK’s HTML.
- **Flask**: Lightweight web dashboard.
- **SQLite**: Built-in DB for result storage.
- **pytest**: Unit testing framework.