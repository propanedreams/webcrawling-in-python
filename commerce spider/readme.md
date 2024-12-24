Enhanced Focused Crawler
Overview

This Python script implements an advanced web crawler designed to scrape product data such as name, price, rating, availability, and description from e-commerce websites. The script respects robots.txt rules, uses depth-based crawling, and saves the extracted data into a CSV file.
Features

    Customizable Crawling: Specify the starting URL (base_url), maximum pages to crawl (max_pages), and depth limit (max_depth).
    Robots.txt Compliance: Automatically checks and respects the crawling rules defined in robots.txt.
    Product Data Extraction: Extracts key product information:
        Product name
        Price
        Rating
        Availability
        Description
    CSV Export: Stores the scraped data in a scraped_products.csv file for further analysis or usage.
    Link Discovery: Identifies and enqueues new links for crawling.
    Graceful Error Handling: Handles HTTP request errors and skips problematic pages.

Requirements

    Python 3.7 or higher
    Required Python libraries:
        requests
        beautifulsoup4

Install the dependencies using pip:

pip install requests beautifulsoup4

Usage

    Modify the Base URL: Update the base_url in the script to the starting page of the website you want to crawl.

    Run the Script: Execute the script in your terminal or IDE:

    python enhanced_focused_crawler.py

    Adjust Parameters (Optional):
        max_pages: Set the maximum number of pages to crawl.
        max_depth: Limit the crawling depth to avoid excessive crawling.

    Check Output: The scraped product data will be saved in a file named scraped_products.csv.

Configuration

To adjust the product data extraction logic, modify the extract_product_data method:

    Update the CSS selectors (class_) based on the target website's HTML structure.

Example:

product_containers = soup.find_all('div', class_='grid-product__content')

Example Output

CSV File: scraped_products.csv

name,price,rating,availability,description
Psalm 23 Unisex Hoodie,436,5.0,In Stock,Cozy and comfortable hoodie with Psalm 23 design.
Another Product,250,4.5,In Stock,Stylish product description here.

Notes

    This script is designed to work on e-commerce websites with a specific HTML structure. You may need to tweak the CSS selectors in extract_product_data to match your target site.
    The script includes a politeness delay of 1 second between requests to avoid overloading the server.
    Ensure you have permission to crawl and scrape the target website to comply with legal and ethical guidelines.

Disclaimer

This script is provided for educational purposes. Always adhere to website terms of service and ensure compliance with web scraping laws in your jurisdiction.
