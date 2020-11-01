# @创建时间 : 2020/10/16 22:52
# @开发作者 : Vixcity
# @文件名称 : 糗百爬图.py
# @开发工具 : PyCharm
import requests
from bs4 import BeautifulSoup
import base64
from io import BytesIO

def getImg(allHtml):
    # 获取到我们需要的img图片
    allImg=allHtml.find_all("img",class_='illustration')
    for index,img in enumerate(allImg):
        # 获取到图片的url
        imgurl = img['src']
        images = requests.get("https:"+imgurl)
        Img64 = base64.b64encode(BytesIO(images.content).read())
        imgdata = base64.b64decode(Img64)
        # 这两个代码不知道为啥不行,就用了其他的库
        # 下面两句代码好像转base64编码出错
        # Img64 = base64.b64encode(requests.get("https:"+imgurl).content)
        # print(requests.get("https:"+imgurl).content)
        with open('D:\\python学习\\day01\\爬虫\\choubai\\'+str(index)+'.jpg', 'wb') as f:
            f.write(imgdata)

def main():
    # UA伪装请求数据
    url='https://www.qiushibaike.com/imgrank/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    allHtml = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(allHtml,"html.parser")
    getImg(soup)

if __name__ == '__main__':
    main()