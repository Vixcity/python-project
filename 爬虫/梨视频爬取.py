#需求：爬取梨视频的视频数据
import requests
from lxml import etree
import re #导入正则模块
import os #文件夹设置
import random

if not os.path.exists('./梨视频/'):
    os.mkdir('./梨视频/')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

url='https://www.pearvideo.com/category_5'
#解析出视频详情页的url和视频名称
page_text=requests.get(url=url,headers=header).text
tree=etree.HTML(page_text)
li_list=tree.xpath('//*[@id="listvideoListUl"]/li')
fp=open('./lishipin.html','w',encoding='utf-8')
for li in li_list:
    title=li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
    detail_url=li.xpath('./div/a/@href')[0]
    detail_url='https://www.pearvideo.com/'+detail_url
    #对详情页url发起请求
    detail_text=requests.get(url=detail_url,headers=header).text
    #获取contID
    ex='ed = "0",contId = "(.*?)",comment'
    contId=re.findall(ex,detail_text)[0]
    #生成视频地址  PS：ajax请求 且这里的headers要多加一个参数
    video_url='https://www.pearvideo.com/videoStatus.jsp?'
    params = {
        'contId': contId,
        'mrd': str(random.random())
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        ,"Referer": detail_url
    }
    rsp = requests.get(url=video_url, headers=headers, params=params)
    json = rsp.json()
    ## 原ajax请求中存储的地址请求不到视频数据 得对url进行重组 （好狗啊
    #网页中动态加载的视频地址：
    #https://video.pearvideo.com/mp4/third/20201023/cont-1703247-10008579-151057-hd.mp4
    #Ajax请求得到的视频地址：
    #https://video.pearvideo.com/mp4/third/20201023/1603677028176-10008579-151057-hd.mp4
    if "videoInfo" in json.keys():
        srcUrl = json['videoInfo']['videos']['srcUrl']
        print(srcUrl)
        title1 = '/'.join(srcUrl.split('/')[0:-1])#取出https://video.pearvideo.com/mp4/third/20201023
        body = "/cont-" + contId + '-'#得到cont-1703247-
        footer = '-'.join(srcUrl.split('-')[1:])#取出10008579-151057-hd.mp4
        srcUrl = title1 + body + footer#组合
        print(srcUrl)
    #下载视频  持久化存储
    data=requests.get(url=srcUrl,headers=header).content
    with open('./梨视频/'+title,"wb") as fp:
        fp.write(data)
    print(title+'下载成功！！')