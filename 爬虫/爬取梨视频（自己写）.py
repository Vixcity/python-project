import os
import re
import time
import random
import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor

ua = UserAgent()
headers = {
    "User-Agent": ua.chrome
}
url = 'https://www.pearvideo.com/category_5'

# 创建文件夹
if not os.path.exists('./梨视频/'):
    os.mkdir('./梨视频/')


def getUrlPage():
    html = pq(requests.get(url=url, headers=headers).text)
    detail_urls = html('#listvideoListUl .vervideo-bd>a')
    detail_page_urls = []
    for detail_page_url in detail_urls:
        detail_page_urls.append('https://www.pearvideo.com/' + pq(detail_page_url).attr('href'))
    return detail_page_urls


def getDetailPage(url_list):
    videoUrl = []
    for url in url_list:
        response = requests.get(url=url, headers=headers).text
        ex = 'isFavorited = "0",contId = "(.*?)",comment'
        contId = re.findall(ex, response)[0]
        header = {
            "User-Agent": ua.chrome,
            "Referer": 'https://www.pearvideo.com/video_' + contId
        }
        data = {
            "contId": contId,
            "mrd": str(random.random())
        }
        requestUrl = 'https://www.pearvideo.com/videoStatus.jsp?'
        videoUrl.append({
            'headers': header,
            'params': data,
            'url': requestUrl,
            "contId": contId,
        })
        executor = ThreadPoolExecutor(max_workers=4)
        print('开始下载')
        # 用法: 函数 和 可迭代参数，类似字典和列表
        executor.map(getVideoSrc, videoUrl)


def getVideoSrc(obj):
    rsp = requests.get(url=obj["url"], headers=obj["headers"], params=obj["params"])
    json = rsp.json()
    videoUrl = json["videoInfo"]['videos']["srcUrl"]
    title = '/'.join(videoUrl.split('/')[0:-1])
    body = "/cont-" + obj["contId"] + '-'
    footer = '-'.join(videoUrl.split('-')[1:])
    # https://video.pearvideo.com/mp4/third/20201104/cont-1705254-10008579-163422-hd.mp4
    # https://video.pearvideo.com/mp4/third/20201104/1604562013191-10008579-163422-hd.mp4
    videoUrl = title + body + footer
    data = requests.get(url=videoUrl, headers=headers).content
    with open('./梨视频/' + obj["contId"] + '.mp4', "wb") as fp:
        fp.write(data)
        print(obj["contId"] + '下载成功！！')


def main():
    url_list = getUrlPage()
    getDetailPage(url_list)


if __name__ == '__main__':
    main()
# 代码有点冗余，望改进
