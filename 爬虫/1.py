# @创建时间 : 2020/10/4 19:13
# @开发作者 : Vixcity
# @文件名称 : 1.py
# @开发工具 : PyCharm

import requests
# from multiprocessing.dummy import Pool 线程池
if __name__ == "__main__":
    url='https://www.sogou.com/'
    respon = requests.get(url=url)
    page_text = respon.text
    print(page_text)
    with open('./sougou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)