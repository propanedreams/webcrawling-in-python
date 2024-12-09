import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
from time import sleep

class WebCrawler:
    def __init__(self, base_url, max_pages=10):
        self.base_url = base_url
        self.max_pages = max_pages
        self.visited = set()
        self.to_visit = [base_url]
        self.robot_parsers = {}  # Cache for robot parsers
    
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
                print(f"Error reading robots.txt from {robots_url}: {e}")
                self.robot_parsers[domain] = None
        
        parser = self.robot_parsers.get(domain)
        if parser:
            return parser.can_fetch("*", url)  # "*" matches any user-agent
        return True  # Assume allowed if robots.txt is not found or fails to load
    
    def crawl(self):
        while self.to_visit and len(self.visited) < self.max_pages:
            current_url = self.to_visit.pop(0)
            if current_url in self.visited:
                continue
            
            if not self.is_allowed_by_robots(current_url):
                print(f"Blocked by robots.txt: {current_url}")
                continue
            
            print(f"Crawling: {current_url}")
            try:
                response = requests.get(current_url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    self.visited.add(current_url)
                    
                    # Extract and enqueue new links
                    for link in soup.find_all('a', href=True):
                        full_url = urljoin(current_url, link['href'])
                        if full_url not in self.visited and full_url.startswith("http"):
                            self.to_visit.append(full_url)
            except Exception as e:
                print(f"Error crawling {current_url}: {e}")
            
            sleep(1)  # sleep to avoid overloading servers, it is the polite thing to do.. and my spider must be polite
        
        print(f"Crawled {len(self.visited)} pages.")

# Example usage
crawler = WebCrawler(base_url="https://en.wikipedia.org/wiki/Main_Page", max_pages=20)
crawler.crawl()
