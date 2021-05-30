import os

import requests
from bs4 import BeautifulSoup

url = "https://vecka.nu/"

br = requests.get(url, headers={"User-agent": "Chrome"})
sr = br.content
bf = BeautifulSoup(sr, "html.parser")
v = int(bf.find("time").text)

os.system("echo %d > index.html" % v)
