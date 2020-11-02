from requests_html import HTMLSession
import pandas as pd

session = HTMLSession()
url = 'https://www.jianshu.com/p/85f4624485b9'
# 获取网页
r = session.get(url)
# 节点选择，右击，copy selector，粘贴
sel = '#__next > div._21bLU4._3kbg6I > div > div._gp-ck > section:nth-child(1) > article > p > a'
# 找到对应的节点
results = r.html.find(sel)
# 筛选节点获取名字和连接
def get_text_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            mylink = list(result.absolute_links)[0]
            mylist.append((mytext, mylink))
        return mylist
    except:
        return None
# 数据框显示
df = pd.DataFrame(get_text_link_from_sel(sel))
# 添加标题
df.columns = ['标题', '链接']
# 导出excel表格
df.to_csv('output.csv', encoding='gbk', index=False)