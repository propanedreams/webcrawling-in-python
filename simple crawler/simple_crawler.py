import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep

def crawl(url, max_pages=10):
    visited = set()
    to_visit = [url]
    
    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue
        
        print(f"Crawling: {current_url}")
        response = requests.get(current_url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            visited.add(current_url)
            
            # Extract links
            for link in soup.find_all('a', href=True):
                full_url = urljoin(current_url, link['href'])
                if full_url not in visited and full_url.startswith("http"):
                    to_visit.append(full_url)
        
        sleep(1)  # Be polite and avoid overloading the server
    
    print(f"Crawled {len(visited)} pages.")

# Start crawling
crawl("https://example.com")
