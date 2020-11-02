# @创建时间 : 2020/9/22 20:22
# @开发作者 : Vixcity
# @文件名称 : VIP.py
# @开发工具 : PyCharm

import webbrowser
webbrowser.open('https://www.iqiyi.com/')
url = input('请输入你想要输入的视频网址:')
vipUrl = 'http://www.wmxz.wang/video.php?url='
webbrowser.open(vipUrl+url)
print(vipUrl+url)
