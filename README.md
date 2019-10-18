# CXPyQt4HTTP


嫌麻烦自己封装的简单请求类，目前已实现异步请求

例子
~~~

import HttpRequestUtils
from PyQt4 import QtCore,QtGui

class Widget(QtGui.QMainWindow):

def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)

def initUI(self, WEBData):
    self.setGeometry(300, 200, 600, 600)
    self.setWindowTitle(WEBData)
    #添加网络请求
    thread = RequestThread()
    thread.requestURL = "https://www.apiopen.top/femaleNameApi"
    thread.requestData = {
    'page': 1
    }
    thread.requestState = 'get'
    thread.trigger.connect(self.changeValue)
    #请求开始
    thread.start()

    self.show()

def changeValue(self, dic):
    print "回传成功"
    print dic
    self.setWindowTitle(str(dic['code']))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    widget.initUI(sys.argv[0])
    widget.show()
    sys.exit(app.exec_())

~~~


