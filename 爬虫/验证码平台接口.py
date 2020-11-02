from io import BytesIO
import json
import base64
import requests
from pyquery import PyQuery as pq
from fake_useragent import UserAgent


def base64_api(uname, pwd, b64):
    # with open(img, 'rb') as f:
    #     base64_data = base64.b64encode(f.read())
    #     b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


def main():
    ua = UserAgent()
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    headers={
        "User-Agent": ua.chrome
    }
    respon = requests.get(url=url, headers=headers).text
    html = pq(respon)
    imgSrc = 'https://so.gushiwen.cn'+html('#imgCode').attr('src')
    images = requests.get(imgSrc)
    img = base64.b64encode(BytesIO(images.content).read())
    b64 = str(img, 'utf8')
    result = base64_api(uname='Vixcity', pwd='wx123456.', b64=b64)
    print(result)

if __name__ == "__main__":
    # img_path = "C:/Users/Administrator/Desktop/RandCode.jpg"
    # result = base64_api(uname='Vixcity', pwd='wx123456.', img=img_path)
    # print(result)
    main()
