# @创建时间 : 2020/10/4 19:43
# @开发作者 : Vixcity
# @文件名称 : search.py
# @开发工具 : PyCharm

import requests
url = 'https://www.sogou.com/web?'
searchWord = input('请输入您想要搜索的内容：')
#反爬机制:UA检测
#反反爬策略:UA伪装
header={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
object ={
    'query':searchWord
}
response = requests.get(url=url,params=object,headers=header)
print(response)
page_text = response.text
fileName = searchWord+'.html'
with open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(fileName+'保存成功')