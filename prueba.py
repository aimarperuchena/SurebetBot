import urllib.request
import pymysql
import urlopen
import request
import requests
from bs4 import BeautifulSoup
from datetime import date
import datetime
from urllib.request import Request, urlopen
url = 'http://127.0.0.1:8000/api/surebet'
objeto = {'match': 'asdfasdfasdf', 'date': '2020-12-12', 'team1': 'aaa', 'team2': 'bbb', 'odd1': 1.3, 'odd2': 1.4,
          'odd3': 1.4, 'bookie1_id': 1, 'bookie2_id': 2, 'bookie3_id': 3, 'percentage': 3}
x = requests.post(url, data=objeto)
