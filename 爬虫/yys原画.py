import re
import os
import time
import requests
from bs4 import BeautifulSoup

url = 'https://yys.163.com/media/picture.html'
response = requests.get(url).content.decode('utf-8')
soup = BeautifulSoup(response, 'lxml')
wallpaper = soup.find_all('div', {'class': 'tab-cont'})  # 横板加竖版

pc = wallpaper[0].find_all('div', {'class': 'mask'})  # 横版图片
mo = wallpaper[1].find_all('div', {'class': 'mask'})  # 竖版图片

pc_list = []  # 新建一个空列表存放横版1920*1080的图片
for i in range(len(pc)):
    a = pc[i].find_all('a')
    if len(a) == 6:
        url = re.findall('href="(.*?)" target', str(a[3]))[0]  # 提取1920*1080的图片地址
        pc_list.append(url)
    elif len(a) == 5:
        url = re.findall('href="(.*?)" target', str(a[2]))[0]
        pc_list.append(url)
    elif len(a) == 4:
        url = re.findall('href="(.*?)" target', str(a[1]))[0]
        pc_list.append(url)
    elif len(a) == 3:
        url = re.findall('href="(.*?)" target', str(a[0]))[0]
        pc_list.append(url)

if not os.path.exists('demo/横版19201080'):
    os.makedirs('demo/横版19201080')
os.chdir('demo/横版19201080')

for i in range(len(pc_list)):
    time.sleep(0.3)  # 爬取延时，防止被察觉，远程关闭连接
    img = requests.get(pc_list[i])
    if img.status_code == 200:
        open(f'{i}.jpg', 'wb').write(img.content)
        print(f'{i} 下载成功')
    else:
        print(f'{i} 下载失败  原因：{img.status_code}')
