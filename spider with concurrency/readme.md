# Web Crawler with SQLite Storage and Robots.txt Compliance

## Overview

This Python web crawler efficiently visits web pages starting from a base URL, extracts useful data, and stores it in an SQLite database. It is designed to respect `robots.txt` rules and includes options for concurrency and data extraction.

---

## Features

### Core Functionality
- **Page Crawling**:
  - Crawls up to a user-defined number of pages (`max_pages`) starting from a base URL.
  - Respects `robots.txt` directives to avoid crawling restricted pages.
- **Concurrency**:
  - Uses multithreading to crawl pages in parallel (`max_workers` threads).

### Data Extraction
- Extracts:
  - **Title**: Page title.
  - **Meta Description**: Content of the meta description tag.
  - **H1 Tags**: All `<h1>` tags as a comma-separated string.
  - **Links**: All valid outbound links.
  - **Images**: Image URLs with associated alt text.
  - **Tables**: Text content of all tables.

### Data Storage
- Saves the extracted data into an SQLite database (`visited_sites.db`) with the following fields:
  - `id`: Unique identifier for each page.
  - `url`: URL of the crawled page.
  - `title`: Page title.
  - `meta_description`: Meta description content.
  - `h1_tags`: Extracted H1 tags.
  - `links`: Outbound links.
  - `images`: Image URLs with alt text.
  - `tables`: Table contents.
  - `timestamp`: Timestamp of the crawl.

### Logging
- Logs detailed activity, including errors and status updates, to a log file (`crawler.log`).

---

## Requirements

- Python 3.x
- Required libraries:
  - `requests`
  - `beautifulsoup4`

Install the dependencies using:
```bash
pip install requests beautifulsoup4



running

python crawler.py https://example.com --max_pages 50 --max_workers 10
