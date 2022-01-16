import requests
from bs4 import BeautifulSoup
import re
with open("filtered-urls.txt") as f:
    urls = f.readlines()

fopen = open("anchor-rss.txt", "a+")
href_regex = r"href=\"(.*?)\""
for url in urls:
    r = requests.get("https://" + url.strip())
    soup = BeautifulSoup(r.content, 'html.parser')
    find_rss = soup.find('link', type='application/rss+xml')
    rss = re.search(href_regex, str(find_rss))
    try:
        fopen.write(rss.group(1) + "\n")
        print(rss.group(1))
    except Exception as e:
        print(e)
