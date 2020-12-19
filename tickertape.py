import time
import requests
from bs4 import BeautifulSoup
from lxml import html
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
class TickerTape:
    def __init__(self):
        ulr = "https://www.tickertape.in/screener/"
        print("Collecting data...")
        self.settingup(url)


    def settingup(self,url):
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        tree = html.fromstring(page.content)
        table = soup.find(class_="selected-filters")
        stock_universe = table.findAll(class_ = "sc-checkbox default").click()
        



