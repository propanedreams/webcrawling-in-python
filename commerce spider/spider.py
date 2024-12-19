import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import csv
import time

class FocusedCrawler:
    def __init__(self, base_url, max_pages=10):
        self.base_url = base_url
        self.visited = set()
        self.to_visit = [base_url]
        self.max_pages = max_pages

    def crawl(self):
        while self.to_visit and len(self.visited) < self.max_pages:
            url = self.to_visit.pop(0)
            if url in self.visited:
                continue

            print(f"Crawling: {url}")
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    self.visited.add(url)
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Focused scraping: extracting product data
                    for product in soup.find_all('div', class_='product-item'):
                        name = product.find('h2').text.strip()
                        price = product.find('span', class_='price').text.strip()
                        print(f"Product: {name} - Price: {price}")

                    # Find links to other product pages
                    for link in soup.find_all('a', href=True):
                        if "product" in link['href']:
                            full_url = urljoin(url, link['href'])
                            if full_url not in self.visited:
                                self.to_visit.append(full_url)
            except Exception as e:
                print(f"Error crawling {url}: {e}")

# Example usage
crawler = FocusedCrawler(base_url="https://example-ecommerce-site.com", max_pages=5)
crawler.crawl()