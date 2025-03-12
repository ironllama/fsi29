import requests
from bs4 import BeautifulSoup

kh = requests.get("https://www.koreaherald.com/")

soup = BeautifulSoup(kh.text, 'html.parser')

for i, read in enumerate(soup.select("article.most_popular p.ellipsis2")):
    print(f"[{i+1}] {read.text}")
