# @创建时间 : 2020/10/4 20:19
# @开发作者 : Vixcity
# @文件名称 : 百度翻译.py
# @开发工具 : PyCharm

import requests
import json

post_url = 'https://fanyi.baidu.com/sug'
kw = input('请输入您想要翻译的内容:')
# UA伪装
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
data = {
    'kw': kw
}
response = requests.post(url=post_url, data=data, headers=header)
obj = response.json()
fp = open('./' + kw + '.json', 'w', encoding='utf-8')
json.dump(obj, fp=fp, ensure_ascii=False)
print('over')
