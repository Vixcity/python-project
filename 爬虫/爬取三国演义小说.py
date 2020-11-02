# 目录地址 url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# UA 伪装 和 请求地址
ua = UserAgent()
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
api_url = "http://dps.kdlapi.com/api/getdps/?orderid=940352463314895&num=1&pt=1&sep=1"
proxy_ip = requests.get(api_url).text
username = "2091283625"
password = "kc6kh20i"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
}
headers = {
    "User-Agent":ua.chrome
}

# 获取到页面的内容
def getHtml():
    # 获取章节目录的网页内容
    HTML = requests.get(url=url, headers=headers,proxies=proxies).text

    # BeautifulSoup实例化
    soup = BeautifulSoup(HTML, 'lxml')

    # 获取章节名所在的a标签
    SectionTitlesTag = soup.select('.book-mulu a')
    f = open('三国演义.txt', 'a', encoding='utf-8')
    for index,i in enumerate(SectionTitlesTag):
        # 标题名 和 标题链接
        SectionTitles = i.text
        contentUrl = 'https://www.shicimingju.com' + i.get('href')

        # 写入标题
        f.write(SectionTitles)
        f.write('\n')

        # 获取正文内容
        content = requests.get(url=contentUrl,headers=headers,proxies=proxies).text
        soup1 = BeautifulSoup(content, 'lxml')
        chapter_content = soup1.select('.chapter_content p')

        # 写入正文内容
        for i in chapter_content:
            f.write(i.text)
            f.write('\n')

        print('已加载完第', index+1, '章')

def main():
    getHtml()

if __name__ == '__main__':
    main()