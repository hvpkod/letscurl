import os

import requests
from bs4 import BeautifulSoup

url = "https://www.dagensnamn.nu/"

br = requests.get(url, headers={"User-agent": "Chrome"})
sr = br.content
bf = BeautifulSoup(sr, "html.parser")
v = bf.find("h1").text

os.system("echo %s > namnsdag/index.html" % v)
