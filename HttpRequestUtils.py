# -*- coding: utf-8 -*-
import requests
import json
import hashlib
import random
import time
from PIL import Image
from PyQt4 import QtGui
from PyQt4 import QtCore


# 提供Get请求方法
# URL: 请求地址  Data: 请求参数  fn: 请求回调(方法)
def requestGetHttp(URL, Data, fn):
    # 请求地址
    requestURL = URL

    # 请求参数
    requestData = Data

    # 请求header
    requestHeaders = ABOOHeaderData()

    # 开始请求
    response = requests.get(requestURL, params=requestData, headers=requestHeaders)

    # 将请求的数据解析
    try:
        jsonData = json.loads(response.text)
    except ValueError:
        jsonData = response.text

    print jsonData

    # 回传数据
    fn(jsonData, response.status_code)


# 提供Post请求方法
# URL: 请求地址  Data: 请求参数  fn: 请求回调(方法)
def requestPostHttp(URL, Data, fn):

    # 请求地址
    requestURL = URL

    # 请求参数
    requestData = Data

    # 请求header
    requestHeaders = ABOOHeaderData()

    # 开始请求
    response = requests.post(requestURL, params=requestData, headers=requestHeaders)

    # 将请求的数据解析
    try:
        jsonData = json.loads(response.text)
    except ValueError:
        jsonData = response.text

    print jsonData

    # 回传数据
    fn(jsonData, response.status_code)


# 生成header
def ABOOHeaderData():
 
    # back header
    backHeaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-type": "application/json",
    }

    return backHeaders


# 下载网络图片(同步)
# ImageURL: 图片地址  Obj: pyqt控件
def download_img(ImageURL, Obj):
    if ImageURL and type(Obj) == QtGui.QLabel:
        print("-----------正在下载图片 ")
        # 这是一个图片的url
        try:
            url = ImageURL
            response = requests.get(url)
            # 获取的文本实际上是图片的二进制文本
            img = response.content
            # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本

            pathNumber = random.randint(1, 99)
            localtime = time.localtime(time.time())
            pathTime = "{}{}{}{}{}{}{}".format(localtime[0], localtime[1], localtime[2], localtime[3], localtime[4], localtime[5], localtime[6])
            ImageName = "{}{}".format(pathTime, pathNumber)

            # 保存路径
            path = 'D:/Documents/ABOO/jpg/{}.jpg'.format(ImageName)
            with open(path, 'wb') as f:
                f.write(img)

            # 下载完成后转换格式
            img = Image.open(path)
            img.save('D:/Documents/ABOO/png/{}.png'.format(ImageName))

            # 加载图片\
            Obj.setStyleSheet(QtCore.QString.fromUtf8("border-image: url(D:/Documents/ABOO/png/{}.png);".format(ImageName)))

        except Exception as ex:
            print("--------出错继续----")
            pass


