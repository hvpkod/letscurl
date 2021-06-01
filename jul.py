import datetime
import os
from datetime import date

year = datetime.date.today().year
month = datetime.date.today().month
day = datetime.date.today().day
today = date(year, month, day)
julafton = date(year, 12, 24)
delta = julafton - today
delta = delta.days

os.system("echo %d > out/jul" % delta)
