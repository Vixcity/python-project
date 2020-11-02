import requests
import json
from bs4 import BeautifulSoup

# 请求
def start_requests(url):
    r=requests.get(url)
    return r.content

# 解析
def parse(text):
    soup = BeautifulSoup(text, 'lxml')
    infos = soup.find_all('li', attrs={'class': 'j_thread_list'})
    for info in infos[1:]:
        mydict = {}
        mydict['title'] = info.find('a', class_='j_th_tit').text.strip()
        mydict['link'] = "http://tieba.baidu.com/" + info.find('a', class_='j_th_tit')['href']
        mydict['author'] = info.find('a', class_='frs-author-name').text.strip()
        mydict['time'] = info.find('span', class_='pull-right').text
        result_list.append(mydict)
    next_page = soup.find('a', class_='next')
    if next_page:
        next_url = 'http:' + next_page['href']
        print(next_url)
        text = start_requests(next_url)
        parse(text)

# 写入
def write_json(result):
    s = json.dumps(result, indent=4, ensure_ascii=False)
    with open('D:\\pycharm\\demo\\tieba.json', 'w', encoding='utf-8') as f:
        f.write(s)

# 执行
def main():
    text = start_requests(base_url)
    parse(text)
    write_json(result_list)
    print('写入完成')

if __name__ == '__main__':
    base_url = 'https://tieba.baidu.com/f?ie=utf-8&kw=python&fr=search'
    result_list = []
    main()