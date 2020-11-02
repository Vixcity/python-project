import os
import re
import time
import requests
from bs4 import BeautifulSoup


def url_get():
    url = 'https://yys.163.com/media/video.html'
    response = requests.get(url).content.decode('utf-8')
    soup = BeautifulSoup(response, 'lxml')
    video = soup.find_all('div', {'class': 'tab-cont'})  # 阴阳师、式神、剧情、其它
    return video


def info_get(video):
    title = re.findall('<div class="title">(.*?)</div>', str(video[1]))  # 视频名称
    href = re.findall('href="(.*?)"', str(video[1]))  # 视频链接
    for name, link in zip(title, href):
        video_save(name, link)


def video_save(name, link):
    time.sleep(0.3)
    movie = requests.get(link)
    if movie.status_code == 200:
        open(f'{name}.mp4', 'wb').write(movie.content)
        print(f'{name} 下载成功')
    else:
        print(f'{name} 下载失败  原因：{movie.status_code}')


if __name__ == '__main__':
    if not os.path.exists('demo/式神视频'):
        os.mkdir('demo/式神视频')
    os.chdir('demo/式神视频')
    video = url_get()
    info_get(video)

