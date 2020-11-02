import os
import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent

ua = UserAgent()
url = 'http://pic.netbian.com/4kmeinv/'
headers = {
    "User-Agent": ua.chrome
}


def Pyquery():
    html = pq(url=url)
    lista = html('ul.clearfix li a')
    # 如果没有文件夹，那么就创建一个
    if not os.path.exists('demo/4k壁纸'):
        os.mkdir('demo/4k壁纸')

    for index, a in enumerate(lista):
        src = 'http://pic.netbian.com/' + a.attrib['href']

        # 打开图片详情网址
        imghtml = pq(url=src)
        imgElement = imghtml('a#img img')
        imgSrc = 'http://pic.netbian.com/' + imgElement.attr('src')
        imgName = imgElement.attr('title')

        # 编码解码
        imgName = imgName.encode('iso-8859-1').decode('gbk')

        # 获取图片
        imgdata = requests.get(url=imgSrc, headers=headers).content
        imgPath = 'demo/4k壁纸/' + imgName + '.jpg'
        with open(imgPath, 'wb') as f:
            f.write(imgdata)
            print(imgName, '下载成功!!!')


def main():
    Pyquery()


if __name__ == "__main__":
    main()
