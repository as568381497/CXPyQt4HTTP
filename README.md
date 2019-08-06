# CXPyQt4HTTP


PyQt4x下的网络请求，自己封装了一下，好用一点

PyQt是不支持网络图片的，所以自己加了个能够下载网上网络图片的方法，优点是可以下载网上了各种网络图片，在本地控件上显示，其实也是从网上下载，然后转换为本地可以显示的图片格式。缺点是，目前方法是同步的，异步处理需要后续研究了加上，还有很大的优化空间

~~~

一、使用前导入相关库
1.requests
2.PIL

二、导入头文件
import requests
import json
import hashlib
import random
import time
from PIL import Image
from PyQt4 import QtGui
from PyQt4 import QtCore

~~~

然后就可以了
