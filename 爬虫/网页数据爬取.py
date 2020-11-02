import requests
from pyquery import PyQuery as pq


def get_page(url):
    """发起请求 获得源码"""
    r = requests.get(url)
    r.encoding = 'utf8'
    html = r.text
    return html


def parse(text):
    """解析数据 写入文件"""
    doc = pq(text)
    # 获得每一行的tr标签
    tds = doc('table.rk-table tbody tr').items()
    for td in tds:
        rank = td.find('td:first-child').text()     # 排名
        name = td.find('td.align-left').text()      # 大学名称
        city = td.find('td:nth-child(3)').text()    # 城市
        type = td.find('td:nth-child(4)').text()    # 类型
        score = td.find('td:nth-child(4)').text()   # 总分
        with open('D:\\pycharm\\demo\\collage.scv', 'a+', encoding='utf8') as f:
            f.write(rank + '\t\t')
            f.write(name + '\t\t')
            f.write(city + '\t\t')
            f.write(type + '\t\t')
            f.write(score + '\t\t\n')
    print("写入完成")


if __name__ == "__main__":
    url = "https://www.shanghairanking.cn/rankings/bcur/2020"
    text = get_page(url)
    parse(text)