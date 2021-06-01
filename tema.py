import os

import requests
from bs4 import BeautifulSoup

url = "https://temadagar.se/"

br = requests.get(url, headers={"User-agent": "Chrome"})
sr = br.content
bf = BeautifulSoup(sr, "html.parser")
v = []

for f in bf.find("center"):
    v.append(f.text)

v = list(filter(None, v))

os.system("echo %s > out/tema" % v)
