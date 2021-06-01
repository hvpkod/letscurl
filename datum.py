import os
from datetime import date

today = date.today()

os.system("echo %s > out/datum" % today)
