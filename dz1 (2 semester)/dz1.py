import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

headers = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}

result_links = {}

data = requests.get('https://ru.wikipedia.org/api/rest_v1/page/random/summary', headers=headers).json()
page_url = data['content_urls']['desktop']['page']

req = requests.get(page_url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
main_content = soup.find(id='mw-content-text')

count = 0
for paragraph in main_content.find_all('p'):
    for link in paragraph.find_all('a', href=True):
        url = link['href']
        name = link.get('title')

        if name and url.startswith('/wiki/') and ':' not in url:
            result_links[name] = urljoin(page_url, url)
            count += 1

        if count == 3:
            break

    if count == 3:
        break

print(result_links)