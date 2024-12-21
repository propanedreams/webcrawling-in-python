import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
import csv
import time

class EnhancedFocusedCrawler:
    def __init__(self, base_url, max_pages=50, max_depth=3):
        self.base_url = base_url
        self.max_pages = max_pages
        self.max_depth = max_depth
        self.visited = set()
        self.to_visit = [(base_url, 0)]  # (url, depth)
        self.scraped_data = []
        self.robot_parsers = {}  # Cache for robot parsers

    def fetch_page(self, url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def save_data_to_csv(self, filename):
        """Saves scraped data to a CSV file."""
        keys = ["name", "price", "rating", "availability", "description"]
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(self.scraped_data)

    def is_allowed_by_robots(self, url):
        """Checks robots.txt rules."""
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
                print(f"Error reading robots.txt from {robots_url}: {e}")
                self.robot_parsers[domain] = None
        parser = self.robot_parsers.get(domain)
        if parser:
            return parser.can_fetch("*", url)  # "*" matches any user-agent
        return True  # Assume allowed if robots.txt is not found or fails to load

    def extract_product_data(self, soup):
        """Extracts product data."""
        product_list = []
        #make a list for each element which is needed, ; product = bunch of generic tags used for it, iterate untill value hit
        for product in soup.find_all('div', class_='product-item'):
            name = product.find('h2', class_='product-name').get_text(strip=True) if product.find('h2', class_='product-name') else "No name"
            price = product.find('span', class_='price').get_text(strip=True) if product.find('span', class_='price') else "No price"
            rating = product.find('div', class_='rating').get_text(strip=True) if product.find('div', class_='rating') else "No rating"
            availability = product.find('span', class_='availability').get_text(strip=True) if product.find('span', class_='availability') else "No availability"
            description = product.find('p', class_='description').get_text(strip=True) if product.find('p', class_='description') else "No description"
            product_list.append({
                "name": name,
                "price": price,
                "rating": rating,
                "availability": availability,
                "description": description
            })
        return product_list

    def crawl(self):
        while self.to_visit and len(self.visited) < self.max_pages:
            url, depth = self.to_visit.pop(0)
            if url in self.visited or depth > self.max_depth:
                continue
            # Check robots.txt
            if not self.is_allowed_by_robots(url):
                print(f"Blocked by robots.txt: {url}")
                continue

            print(f"Crawling: {url} at depth {depth}")
            soup = self.fetch_page(url)
            if not soup:
                continue

            self.visited.add(url)

            # Extract and save product data
            products = self.extract_product_data(soup)
            self.scraped_data.extend(products)

            # Extract links for further crawling
            for link in soup.find_all('a', href=True):
                full_url = urljoin(url, link['href'])
                if full_url not in self.visited and full_url.startswith("http"):
                    self.to_visit.append((full_url, depth + 1))

            # Pause to avoid overloading the server
            time.sleep(1)

        # Save the scraped data to a CSV file
        self.save_data_to_csv("scraped_products.csv")
        print(f"Crawling finished. Scraped {len(self.scraped_data)} products. Data saved to 'scraped_products.csv'.")
# Example usage
crawler =  EnhancedFocusedCrawler(base_url="https://elevatedfaith.com/", max_pages=5)
crawler.crawl()