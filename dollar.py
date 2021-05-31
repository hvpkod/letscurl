import os

import requests
from bs4 import BeautifulSoup

url = "https://www.avanza.se/index/om-indexet.html/19000/usd-sek"

br = requests.get(url, headers={"User-agent": "Chrome"})
sr = br.content
bf = BeautifulSoup(sr, "html.parser")
v = bf.find("td", {"class": None}).text

os.system("echo %s > out/dollar" % v)
