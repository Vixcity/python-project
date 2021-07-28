import requests
import os
import pprint

url = 'https://yys.res.netease.com/pc/zt/20161108171335/js/app/all_shishen.json'
if not os.path.exists('demo/阴阳师皮肤'):
    os.makedirs('demo/阴阳师皮肤')
path = 'demo/阴阳师皮肤/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}


def download(name, response):
    with open(path + name, mode='wb') as f:
        f.write(response.content)


response = requests.get(url=url, headers=headers)
html_data = response.json()
for i in html_data:
    num_id = i['id']
    name = i['name']

    beforeAwake = 'https://yys.res.netease.com/pc/zt/20161108171335/data/shishen_big_beforeAwake/{}.png'.format(num_id)
    afterAwake = 'https://yys.res.netease.com/pc/zt/20161108171335/data/shishen_big_afterAwake/{}.png'.format(num_id)
    skin = 'https://yys.res.netease.com/pc/zt/20161108171335/data/shishen_skin/{}-1.png'.format(num_id)

    beforeAwake_response = requests.get(url=beforeAwake, headers=headers)
    beforeAwake_name = name + '初始' + '.png'
    download(beforeAwake_name, beforeAwake_response)

    afterAwake_response = requests.get(url=beforeAwake, headers=headers)
    afterAwake_name = name + '觉醒' + '.png'
    download(afterAwake_name, afterAwake_response)

    skin_response = requests.get(url=beforeAwake, headers=headers)
    skin_name = name + '皮肤' + '.png'
    download(skin_name, skin_response)
    print('正在下载{}图鉴'.format(name))