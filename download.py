"""
@author: YTSakura
@file: download.py
一系列下载
"""
import requests
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 "
                         "Safari/537.36"}
path = './img/'
img_count = 1
img_url = 'http://www.dmoe.cc/random.php'


# 下载图片
def get_img(url=img_url):
    global img_count
    r = requests.get(url, headers=headers).content
    with open(path + str(img_count) + '.jpg', 'wb') as f:
        f.write(r)
    print("第{}张图片下载完成".format(img_count))
    img_count += 1
    return True
