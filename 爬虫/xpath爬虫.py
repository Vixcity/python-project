import requests
from lxml import etree
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
from fake_useragent import UserAgent

ua = UserAgent()

url = 'https://hz.58.com/xihuqu/ershoufang/?utm_source=sem-sales-baidu-pc&spm=62851881867.16537920592&utm_campaign=sell&utm_medium=cpc&showpjs=pc_fg&PGTID=0d30000c-0004-f0a2-62bf-52886ad31056&ClickID=1'
headers = {
    "User-Agent": ua.chrome
}


def Xpath():
    respon = requests.get(url=url, headers=headers).text
    tree = etree.HTML(respon)
    name = tree.xpath('//ul[@class="house-list-wrap"]//h2[@class="title"]/a')
    price = tree.xpath('//p[@class="sum"]/b')
    f = open('58二手房源和价格.txt', 'a', encoding='utf-8')
    for index, i in enumerate(name):
        homeName = i.xpath('./text()')[0]
        howMuch = price[index].xpath('./text()')[0]
        f.write('名称:' + homeName + '\t')
        f.write('价格:' + howMuch + '\n')
    f.close()


def Pyquery():
    html = pq(url=url)
    names = html('ul.house-list-wrap h2.title a')
    prices = html('p.sum b')
    f = open('58二手房源和价格.txt', 'a', encoding='utf-8')
    for index, name in enumerate(names):
        f.write('名称:' + name.text + '\t')
        f.write('价格:' + prices[index].text + '\n')
    f.close()


def BeautifulSoups():
    respon = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(respon, 'lxml')
    names = soup.select('ul.house-list-wrap h2.title a')
    prices = soup.select('p.sum b')
    f = open('58二手房源和价格.txt', 'a', encoding='utf-8')
    for index, name in enumerate(names):
        f.write('名称:' + name.text + '\t')
        f.write('价格:' + prices[index].text + '\n')
    f.close()


def main():
    # Xpath()
    # Pyquery()
    BeautifulSoups()


if __name__ == "__main__":
    main()
