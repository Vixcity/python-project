import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome
}
url = "https://www.xuexila.com/lizhii/lizhimingju/c17726.html"


def getZuoYouMing():
    response = requests.get(url=url, headers=headers)
    response.encoding = 'gbk'
    doc = pq(response.text)
    p = doc('#contentText p')
    with open('./座右铭.txt', 'a', encoding='utf-8') as f:
        for index, i in enumerate(p):
            f.write(i.text)
            print('第', index+1, '句话写入完毕')


def main():
    getZuoYouMing()


if __name__ == "__main__":
    main()
