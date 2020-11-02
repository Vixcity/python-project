#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/6 14:29
# @Author  : Xi.He
# @Desc    : 爬王者荣耀皮肤图片

import requests
import os
import time


headers = {
    'proxy': 'https: 59.57.151.126:37749',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

file_dir = "D:\\pycharm\\demo\\王者\\"  # 存储图片的根目录
url = 'https://pvp.qq.com/web201605/js/herolist.json'
response = requests.get(url, headers=headers)
herolist = response.json() # 将源文件转换为一个列表
hero_number = len(herolist) #


# hero_code = herolist[0]['ename']  英雄编号
# hero_name = herolist[0]['cname']  英雄名字
# skin_name = herolist[0]['skin_name'].split('|') 皮肤名字
# print(hero_name)
# print(skin_name)

for i in range(hero_number):
    # 获取英雄皮肤列表
    hero_name = herolist[i]['cname']
    #print(type(hero_name))
    skin_name = herolist[i]['skin_name'].split('|')
    hero_code = herolist[i]['ename']    # 获取英雄编号
    file = file_dir + hero_name
    print(file)
    if os.path.exists(file):
        os.chdir(file)
    else:
        os.mkdir(file)  # 创建文件夹
        os.chdir(file)  # 进入刚创建的文件夹
    for j in range(len(skin_name)):
        file_name = hero_name + '-' + skin_name[j] + '.jpg' # 文件名称
        skin_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(hero_code) + '/' + str(
            hero_code) + '-bigskin-' + str(j + 1) + '.jpg'
        response_skin = requests.get(skin_url, headers=headers)
        time.sleep(0.5)
        print(response_skin.status_code)
        if response_skin.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(response_skin.content)


