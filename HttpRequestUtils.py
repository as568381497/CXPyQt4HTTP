# -*- coding: utf-8 -*-
import requests
import json
from PyQt4 import QtCore


# 下载文件的线程(耗时操作都在这)
class RequestThread(QtCore.QThread):
    # 回传
    trigger = QtCore.pyqtSignal(dict)
    
    # 请求地址
    requestURL = None
    # 请求参数
    requestData = None
    # 请求方式
    requestState = 'get'
    
    def __index__(self):
        super(RequestThread, self).__init__()
    
    # 执行下载
    def run(self):
        # 请求地址
        requestURL = self.requestURL
        
        # 请求参数
        requestData = self.requestData
        
        # 请求header
        requestHeaders = ABOOHeaderData()
        
        if self.requestState == 'get':
            
            # 开始请求
            response = requests.get(requestURL, params=requestData, headers=requestHeaders)
            
            # 将请求的数据解析
            try:
                jsonData = json.loads(response.text)
            except ValueError:
                jsonData = response.text
            
            self.trigger.emit(jsonData)
        
        elif self.requestState == 'post':
            
            # 开始请求
            response = requests.post(requestURL, params=requestData, headers=requestHeaders)
            
            # 将请求的数据解析
            try:
                jsonData = json.loads(response.text)
            except ValueError:
                jsonData = response.text
            
            self.trigger.emit(jsonData)

# 生成header
def ABOOHeaderData():
    # back header
    backHeaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Content-type": "application/json",
    
    }
    
    return backHeaders
