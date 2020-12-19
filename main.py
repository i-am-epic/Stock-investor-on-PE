import time
import requests
from bs4 import BeautifulSoup
from lxml import html

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

investments = []


def line(self):
    l = '-'*110
    print(l+'\n')


n = 1
num = 1


class StockPrediction1:

    def __init__(self, le):
        url = 'https://www.moneycontrol.com/india/stockpricequote/' + le
        print(url)
        self.comp_info(url)

    def comp_info(self, url):
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        tree = html.fromstring(page.content)

        table = soup.find("table", {"class": "pcq_tbl MT10"})
        c_links = []

        for row in table.findAll("tr"):
            cells = row.find("a")
            # link = cells.find("href")

            if cells is not None:
                l = str(cells)
                l = l[23:].split('"')[0]
                c_links.append(l)
        self.valuation(c_links, tree)

    def valuation(self, c_li, tree):
        global n
        global num
        for u in c_li:
            time.sleep(0.5)
            print(n)
            n += 1
            page = requests.get(u, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(class_="pcstname")
            if title == None:
                continue
            title = title.get_text()
            if title == None:
                continue
            elif title == "":
                continue
            valu = soup.find(class_="all_title_sub").get_text()

            if valu != "Charts":
                continue
            cp = soup.find(class_="pcnsb div_live_price_wrap").get_text()
            ltp = cp.split("\n")
            print(title)
            print(ltp[1], ltp[3])
            tec_any = soup.find(class_="mt15 CTR pb20").get_text()
            tec_any = tec_any[277:290].split("\n")
            print(tec_any[0])

            data = [x.text.strip()
                    for x in soup.find_all('div', {'class': 'value_txtfr'})]
            print(data)
            if data == None:
                continue
            pe = data[1]

            ipe = (data[5])
            if pe == '-':
                print("P/E = N/D")
                pe = 100000
                line("")
                continue

            else:
                pe = float(pe)
                print(('P/E = {}').format(pe))

            if ipe == "-":
                print("Industrial P/E = N/D")
                ipe = 100000
            else:
                ipe = float(ipe)
                print(('Industrial P/E = {}').format(ipe))

            if pe < ipe:
                print("GOOD TO INVEST")
                # investments.append(title)

                file1 = open("Invest_in_this_stocks.txt", "a")

                # \n is placed to indicate EOL (End of Line)
                file1.write(str(num))
                file1.write("\n")
                file1.writelines(title)
                file1.write("\n")
                file1.writelines(ltp)
                file1.write("\n")
                file1.write(
                    "-"*120+"\n")
                file1.close()

                num += 1

            else:
                print("NOT RECOMMENDED TO INVEST")
            line("")


if __name__ == '__main__':
    line("")
    print("HELLO WELCOME TO NIKHIL STOCK_INVESTOR BASED ON [P/E]\n")
    line("")
    file1 = open("Invest_in_this_stocks1.txt", "w")
    s = requests.Session()
    s.max_redirects = 30000
    print("PRESS ANY KEY TO BEGIN.........")

    print(
        "\n"*50)
    test_list = [chr(x) for x in range(ord('a'), ord('z') + 1)]

    test_list.append("others")

    for le in test_list:
        #le = le.upper()
        StockPrediction1(le)
        time.sleep(1)
    line("")
    print('\n')

    for i in range(len(investments)):
        print(investments[i])
    print('\n')
    line("")
    q1 = input()
