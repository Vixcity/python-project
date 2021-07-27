import sqlite3
from urllib.parse import urlparse
import matplotlib.pyplot as plt

websiteDict = {}

conn = sqlite3.connect('C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\history')
cursor = conn.execute("select url from urls")

for item in cursor:
    website = urlparse(item[0]).netloc
    count = websiteDict.setdefault(website, 0)
    websiteDict[website] = count + 1

lst_his = sorted(websiteDict.items(), key=lambda x: x[1], reverse=True)

plt.pie(x=[e[1] for e in lst_his[:10]],
        labels=[e[0] for e in lst_his[:10]],
        autopct='%1.2f%%')

plt.savefig('website.jpg')
plt.show()

print('程序执行成功！！')
