import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, unquote
from matplotlib import pyplot as plt
headers = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}

def get_start():
    url = "https://ru.wikipedia.org/api/rest_v1/page/random/summary"
    req = requests.get(url, headers=headers)
    d = req.json()
    t = d['title']
    p = d['content_urls']['desktop']['page']
    return t, p

def get_link(html):
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find(id="mw-content-text")
    if not div:
        return None

    out = div.find(class_="mw-parser-output")
    if not out:
        return None

    for x in out.find_all(['p', 'ul'], recursive=False):
        for s in x.find_all('sup', class_='reference'):
            s.decompose()
        for c in x.find_all('span', class_='coordinates'):
            c.decompose()

        b = 0
        for e in x.descendants:
            if e.name is None:
                b += e.count('(') - e.count(')')
                b += e.count('[') - e.count(']')
                if b < 0:
                    b = 0
            elif e.name == 'a':
                if b == 0:
                    h = e.get('href', '')
                    if h.startswith('/wiki/') and ':' not in unquote(h):
                        return h
    return None

def run():
    t, u = get_start()
    visited = set()
    cur = u
    steps = 0
    while True:
        if cur in visited:
            return "loop", steps
        else:
            visited.add(cur)
        r = requests.get(cur, headers=headers)
        s = BeautifulSoup(r.content, 'lxml')

        ht = s.find(id="firstHeading")
        if ht:
            curr_t = ht.text
        else:
            curr_t = cur.split('/')[-1]
        if curr_t == "Философия":
            return "win", steps



        if steps > 100:
            return "limit", steps

        nxt = get_link(r.content)

        if not nxt:
            return "dead_end", steps

        cur = urljoin(cur, nxt)
        time.sleep(0.1)
        steps += 1



def t(duration_seconds):
    a = list()
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        status, steps = run()
        if status == "win":
            a.append(steps)
    return a


results = t(900)
if results == []:
    print('не получилось')
else:
    plt.figure(figsize=(12, 6))
    min_steps = min(results)
    max_steps = max(results)
    bins = range(min_steps, max_steps + 2)
    plt.hist(results, bins=bins, edgecolor='black')
    plt.xticks(range(min_steps, max_steps + 1))
    plt.title("Гистограмма")
    plt.xlabel("количество шагов до философии")
    plt.ylabel("количество запусков")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("histogram.png")
    plt.close()
    print(results)
