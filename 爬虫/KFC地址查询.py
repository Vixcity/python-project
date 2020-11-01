# @创建时间 : 2020/10/5 14:52
# @开发作者 : Vixcity
# @文件名称 : KFC地址查询.py
# @开发工具 : PyCharm

import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
keyword = input('请输入您要查询的KFC地址:')
obj = {
    'cname': '',
    'pid': '',
    'keyword': keyword,
    'pageIndex': '1',
    'pageSize': '10',
}
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
respone = requests.post(url=url,headers=header,data=obj)
data = respone.json()
fp = open('./KFC.json','w',encoding='utf-8')
json.dump(data,fp=fp,ensure_ascii=False)
print('over')