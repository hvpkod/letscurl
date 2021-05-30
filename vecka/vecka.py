import os

import requests
from bs4 import BeautifulSoup

url = "https://vecka.nu/"

br = requests.get(url, headers={"User-agent": "Chrome"})
sr = br.content
bf = BeautifulSoup(sr, "html.parser")
v = int(bf.find("time").text)

html = """\
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Vecka</title>
  <meta name="Veckor" content="Svenska veckor">


</head>

<body>
{code}
</body>
</html>""".format(
    code=v
)

f = open("index.html", "w+")
f.write(html)
f.close()
