import os

import requests
from bs4 import BeautifulSoup

url = "https://mp.weixin.qq.com/s?__biz=MzA5OTYzODY1Mg==&mid=2247487286&idx=1&sn=0b0ae10037fb74445b9cd07019028be7&chksm=90fe0325a7898a331c87a3a539f8370c34cf729212639dfa75b4496f278229317f47211ef112&scene=38#wechat_redirect"


def geturl():
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    imgs = soup.find_all('img')
    url_list = []
    if imgs is not None:
        for img in imgs:
            if img.get('data-src') is not None:
                print(img['data-src'])
                url_list.append(img['data-src'])
    return url_list


path = os.getcwd()

if __name__ == '__main__':
    url_list = geturl()
    for url in url_list:
        try:
            pic_name = url.split("/")[-2]
            fmt = url.split("/")[-3][-3:]
            resp = requests.get(url).content
            with open(path + '/out/' + pic_name + '.' + fmt, "wb+") as f:
                f.write(resp)
        except Exception as reason:
            print(str(reason))
