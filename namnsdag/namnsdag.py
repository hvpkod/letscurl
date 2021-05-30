import os

import requests
from bs4 import BeautifulSoup

url = "https://www.dagensnamn.nu/"

br = requests.get(url, headers={"User-agent": "Chrome"})
sr = br.content
bf = BeautifulSoup(sr, "html.parser")
v = bf.find("h1").text

html = """\
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Namnsdag</title>
  <meta name="Svenska namnsdagar" content="Dagens namnsdag">

</head>

<body>
{code}
</body>
</html>
""".format(
    code=v
)

f = open("index.html", "w+")
f.write(html)
f.close()
