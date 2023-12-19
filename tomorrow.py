"""
@author: YTSakura
@file: tomorrow.py
@version: 0.1
查询明日是否为上班、调休或者休息
"""
import time
import datetime
import requests
import json
from api import MoonApiDataholiday as MoonApiData, MoonapiSign

# 获取明天日期
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

# AppId
apiId = 154

# Api的Key_id
accessKeyId = 591

# Api的Key_Code
accessKeySecret = 'x3rygqcph8cmb3f7kmdmcyj3'

# 0为简单签名模式, 直接将sign设置为Key Code即可, 1为认证方式二md5签名认证， 2为认证方式二hmac签名认证
signMethod = 0

parameters = {}
signParameters = {}
parameters['keyid'] = accessKeyId
parameters['_t'] = time.time()
# 此处为其他参数
parameters['apid'] = "159"
# 查询的日期
parameters['date'] = tomorrow

# sign
sign = accessKeySecret
if (signMethod == 1):
    sign = MoonapiSign.generateMd5Signature(parameters, accessKeySecret)
elif (signMethod == 2):
    sign = MoonapiSign.generateHmacSHA1Signature(parameters, accessKeySecret)

# 组装URL
strParams = MoonapiSign.getUrlQueryFromParams(parameters)
urlApi = "http://api.moonapi.com/" + str(apiId) + "?" + strParams + "&sign=" + sign
print(urlApi)


def get_data(url=urlApi):
    """
    获取第二天日期类型的信息
    :param url: api地址
    :return: 0、1、2、3
    """
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = MoonApiData.moon_api_dataholiday_from_dict(json.loads(response.text))

    return data.data.info.type
