import os
import requests

url = 'https://pvp.qq.com/web201605/js/herolist.json'
herolist = requests.get(url)  # 获取英雄列表json文件

herolist_json = herolist.json()  # 转化为json格式
hero_name = list(map(lambda x: x['cname'], herolist.json()))  # 提取英雄的名字
hero_number = list(map(lambda x: x['ename'], herolist.json()))  # 提取英雄的编号
hero_skin = []
for item in herolist_json:
    try:
        hero_skin.append(item['skin_name'])  # 提取英雄皮肤名字
    except Exception as e:
        hero_skin.append(item['title'])

if not os.path.exists('demo/王者荣耀皮肤'):
    os.makedirs('demo/王者荣耀皮肤')
os.chdir('demo/王者荣耀皮肤')


# 下载图片
def downloadPic():
    i = 0
    for j in hero_number:
        if not os.path.exists(hero_name[i]):
            # 创建文件夹
            os.mkdir(hero_name[i])
        # 进入创建好的文件夹
        os.chdir(hero_name[i])
        skin_name = hero_skin[i].split('|')
        for k in range(len(skin_name)+1):
            # 拼接url
            onehero_link = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(j) + '/' + str(
                j) + '-bigskin-' + str(k) + '.jpg'
            im = requests.get(onehero_link)  # 请求url
            if im.status_code == 200:
                open(skin_name[k-1] + '.jpg', 'wb').write(im.content)  # 写入文件
        os.chdir('..')
        print(hero_name[i]+'皮肤下载完成')
        i += 1


downloadPic()
