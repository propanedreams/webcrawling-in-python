# Web Crawler with SQLite Database and CSV Export

## Overview

This Python project is a simple web crawler that visits websites, extracts URLs, and saves them to a SQLite database. It respects `robots.txt` rules and ensures ethical crawling practices. Additionally, the script includes functionality to display the crawled data and export it to a CSV file.

---

## Features

1. **Web Crawling**:
   - Starts from a base URL and explores up to a specified number of pages (`max_pages`).
   - Extracts and queues new links found on the pages.

2. **SQLite Database**:
   - Stores visited URLs along with a timestamp.
   - Avoids revisiting already crawled pages using the database and in-memory `visited` set.

3. **Robots.txt Compliance**:
   - Checks each URL against the domain's `robots.txt` file.
   - Ensures the crawler doesn't violate the website's rules.

4. **CSV Export**:
   - Displays crawled data in a tabular format.
   - Provides an option to export the data to a CSV file.

---

## File Structure

### `crawler.py`
- Contains the `WebCrawler` class.
- Implements crawling, database interaction, and `robots.txt` compliance.

### `display_data.py`
- Fetches and displays crawled data from the SQLite database.
- Exports data to a CSV file on user request.

---

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `sqlite3`
  - `csv`

Install required libraries with:
```bash
pip install requests beautifulsoup4
