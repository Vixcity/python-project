import requests
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    "User-Agent": ua.chrome
}
url = 'http://192.168.0.132:9091/webapi/account/login'
url1 = 'http://192.168.0.132:9091/webapi/account/info'
url2 = 'http://127.0.0.1:8080/conversation/list'
data={
    'userName': 'pnuoc',
    'password': 'DBE87E0A798D5DBA32DC27976E343CF5'
}
session = requests.session()

reponse = session.post(url=url, data=data).text
reponse1 = session.get(url=url1, data=data).text
reponse2 = session.get(url=url2, data=data).text
# with open('demo.html', 'w', encoding='utf-8') as f:
#     f.write(reponse2)

