# @创建时间 : 2020/10/5 14:35
# @开发作者 : Vixcity
# @文件名称 : 豆瓣.py
# @开发工具 : PyCharm

import requests
import json

url = 'https://movie.douban.com/j/search_subjects?'
obj = {
    'type': 'movie',
    'tag': '喜剧',
    'sort': 'recommend',
    'page_limit': '100',
    'page_start': '0',
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
response = requests.get(url=url,params=obj,headers=header)
list = response.json()
fp = open('./douban.json','w',encoding='utf-8')
json.dump(list,fp=fp,ensure_ascii=False)
print('over')