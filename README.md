🕸️ Web Crawler with SQLite Storage

A Python-based web crawler that collects data from websites, including their titles, meta descriptions, and H1 tags. The data is stored in an SQLite database for easy retrieval and analysis.
🚀 Features

    🌐 Web Crawling: Visits and indexes web pages starting from a specified base URL.
    📊 Data Collection: Extracts and saves:
        Page URL
        Title tag content
        Meta description content
        H1 tags content
        Timestamp of the crawl
    🤖 Robots.txt Handling: Respects the robots.txt directives of each website.
    🗄️ SQLite Storage: Efficiently stores crawled URLs and metadata in a database.
    📤 Data Export: Option to export stored data to a CSV file.
    ⚙️ Configurable Crawl Depth: Limit the number of pages crawled for performance control.

🛠️ Requirements

    Python 3.8 or newer
    Libraries:
        requests
        beautifulsoup4
        sqlite3

Install the required libraries using pip:

pip install requests beautifulsoup4

📖 Usage
🕵️‍♂️ Web Crawler

    Set the base_url and max_pages parameters in the crawler script.
    Run the crawler:

python web_crawler.py

The crawler will:

    Respect robots.txt restrictions.
    Extract relevant metadata from each visited page.
    Save the crawled data to an SQLite database (visited_sites.db).

📋 Data Viewer and Exporter

    Run the data display script to view the stored data:

python display_data.py

    Optionally, export the data to a CSV file when prompted.

🗃️ Database Schema

The SQLite database (visited_sites.db) is structured as follows:
Column	Type	Description
id	INTEGER	Unique identifier for each record.
url	TEXT	URL of the visited page.
title	TEXT	Title tag content of the page.
meta_description	TEXT	Meta description content of the page.
h1_tags	TEXT	Comma-separated H1 tag contents.
timestamp	DATETIME	Timestamp of when the page was crawled.
🔍 Example
Crawling

Set the base_url in web_crawler.py:

crawler = WebCrawler(base_url="https://example.com", max_pages=10)
crawler.crawl()

Displaying Data

Run the display script:

python display_data.py


Exporting Data

When prompted, type yes to export the data to visited_sites.csv.
⚠️ Limitations

    The crawler may be blocked by certain websites due to IP bans or aggressive rate-limiting.
    It does not execute JavaScript, so content rendered dynamically by JavaScript may not be indexed.
    Ensure compliance with the terms of service for the websites you crawl.

🛠️ Future Enhancements

    🔄 Multi-threading: Add support for parallel crawling.
    📦 Additional Tags: Scrape more structured data, such as Open Graph or JSON-LD.
    🖥️ Front-End Interface: Build a front-end to display and export data.
    🛡️ Proxy Support: Enable crawling with proxies to bypass rate limits or IP bans.

📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
