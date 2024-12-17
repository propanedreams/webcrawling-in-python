import sqlite3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, urlsplit, urlunsplit
from urllib.robotparser import RobotFileParser
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import logging
import argparse
import hashlib

# Configure logging
logging.basicConfig(level=logging.INFO, filename="crawler.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

class WebCrawler:
    HEADERS = {'User-Agent': 'MyWebCrawler/1.0 (+https://example.com/contact)'}
    CRAWL_DELAY = 1  # Default crawl delay in seconds

    def __init__(self, base_url, max_pages=10, max_workers=5):
        self.base_url = base_url
        self.max_pages = max_pages
        self.max_workers = max_workers
        self.visited = set()
        self.to_visit = [self.normalize_url(base_url)]
        self.robot_parsers = {}  # Cache for robot parsers
        self.conn = self.init_db()  # Initialize SQLite database

    def init_db(self):
        conn = sqlite3.connect('visited_sites.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS visited_sites (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE NOT NULL,
                title TEXT,
                meta_description TEXT,
                h1_tags TEXT,
                links TEXT,
                images TEXT,
                tables TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_url ON visited_sites(url)')
        conn.commit()
        return conn

    def save_page_data_to_db(self, url, title, meta_description, h1_tags, links, images, tables):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT OR IGNORE INTO visited_sites (url, title, meta_description, h1_tags, links, images, tables) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (url, title, meta_description, h1_tags, links, images, tables))
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Database error while saving {url}: {e}")

    def fetch_page(self, url):
        try:
            response = requests.get(url, headers=self.HEADERS, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch {url}: {e}")
            return None

    def normalize_url(self, url):
        parts = urlsplit(url)
        return urlunsplit((parts.scheme, parts.netloc, parts.path, '', ''))  # Remove query and fragments

    def is_allowed_by_robots(self, url):
        parsed_url = urlparse(url)
        domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        if domain not in self.robot_parsers:
            robots_url = urljoin(domain, "/robots.txt")
            parser = RobotFileParser()
            parser.set_url(robots_url)
            try:
                parser.read()
                self.robot_parsers[domain] = parser
            except Exception as e:
                logging.warning(f"Error reading robots.txt from {robots_url}: {e}")
                self.robot_parsers[domain] = None
        
        parser = self.robot_parsers.get(domain)
        if parser:
            return parser.can_fetch("*", url)
        return True  # Assume allowed if robots.txt is not found or fails to load

    def extract_page_data(self, soup):
        title = soup.title.string.strip() if soup.title else None

        meta_description = None
        meta_tag = soup.find("meta", attrs={"name": "description"})
        if meta_tag and "content" in meta_tag.attrs:
            meta_description = meta_tag["content"].strip()

        h1_tags = ", ".join([h1.get_text(strip=True) for h1 in soup.find_all("h1")])
        links = ", ".join([a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("http")])
        images = ", ".join([f"{img['src']} (alt: {img.get('alt', 'N/A')})" for img in soup.find_all('img', src=True)])
        tables = "; ".join([str(table.get_text(strip=True)) for table in soup.find_all("table")])

        return title, meta_description, h1_tags, links, images, tables

    def crawl_page(self, url):
        if not self.is_allowed_by_robots(url):
            logging.info(f"Blocked by robots.txt: {url}")
            return
        
        logging.info(f"Crawling: {url}")
        response = self.fetch_page(url)
        if response:
            soup = BeautifulSoup(response.text, 'html.parser')
            self.visited.add(url)
            title, meta_description, h1_tags, links, images, tables = self.extract_page_data(soup)
            self.save_page_data_to_db(url, title, meta_description, h1_tags, links, images, tables)

            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                normalized_url = self.normalize_url(full_url)
                if normalized_url not in self.visited:
                    self.to_visit.append(normalized_url)
        sleep(self.CRAWL_DELAY)

    def crawl(self):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            while self.to_visit and len(self.visited) < self.max_pages:
                current_url = self.to_visit.pop(0)
                executor.submit(self.crawl_page, current_url)

        logging.info(f"Crawled {len(self.visited)} pages.")
        self.conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Crawler with SQLite Storage")
    parser.add_argument('base_url', help="Starting URL for the crawler")
    parser.add_argument('--max_pages', type=int, default=10, help="Maximum number of pages to crawl")
    parser.add_argument('--max_workers', type=int, default=5, help="Number of parallel threads")
    args = parser.parse_args()

    crawler = WebCrawler(base_url=args.base_url, max_pages=args.max_pages, max_workers=args.max_workers)
    crawler.crawl()
