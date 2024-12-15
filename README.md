Web Crawler with SQLite Storage

This is a Python-based web crawler that collects data from websites, including their titles, meta descriptions, and H1 tags. The crawled data is stored in an SQLite database for easy retrieval and analysis.
Features

    Crawling: Visits and indexes web pages starting from a specified base URL.
    Data Collection: Extracts and saves:
        Page URL
        Title tag content
        Meta description content
        H1 tags content
        Timestamp of the crawl
    Robots.txt Handling: Respects the robots.txt directives of each website.
    SQLite Storage: Stores crawled URLs and their associated metadata in a database.
    Data Export: Provides the option to export the stored data to a CSV file.
    Configurable Crawl Depth: Limits the number of pages to crawl for efficiency.

Requirements

    Python 3.8 or newer
    Libraries:
        requests
        beautifulsoup4
        sqlite3

Install the required libraries using pip:

pip install requests beautifulsoup4

How to Use
Web Crawler

    Set the base_url and max_pages parameters in the crawler script.
    Run the script:

python web_crawler.py

The crawler will:

    Respect robots.txt restrictions.
    Extract relevant metadata from each visited page.
    Save the crawled data to an SQLite database (visited_sites.db).

Data Viewer and Exporter

    Use the data display script to view the stored data:

python display_data.py

    Optionally, export the data to a CSV file when prompted.

Database Schema

The SQLite database (visited_sites.db) uses the following schema:
Column	Type	Description
id	INTEGER	Unique identifier for each record.
url	TEXT	URL of the visited page.
title	TEXT	Title tag content of the page.
meta_description	TEXT	Meta description content of the page.
h1_tags	TEXT	Comma-separated H1 tag contents.
timestamp	DATETIME	Timestamp of when the page was crawled.
Example
Crawling

Set base_url in web_crawler.py:

crawler = WebCrawler(base_url="https://example.com", max_pages=10)
crawler.crawl()

Displaying Data

Run the display script:

python display_data.py

Sample output:

ID    URL                             Title               Meta Description        H1 Tags           Timestamp
1     https://example.com             Example Title       Example Meta Desc.     Welcome, About    2024-12-10 10:00:00
2     https://anotherexample.com      Another Title       Another Meta Desc.     Contact, Blog     2024-12-10 10:05:00

Exporting Data

When prompted, type yes to export data to visited_sites.csv.
Limitations

    The crawler may be blocked by certain websites due to IP bans or aggressive rate-limiting.
    Content from JavaScript-rendered pages will not be indexed, as it does not execute JavaScript.
    Ensure compliance with the terms of service for the websites you crawl.

Future Enhancements

    Add support for multi-threaded crawling.
    Implement scraping for additional tags or structured data (e.g., JSON-LD, Open Graph).
    Include a front-end interface for viewing and exporting data.
    Add proxy support for bypassing rate limits or IP bans.

License

This project is licensed under the MIT License. See the LICENSE file for details.
