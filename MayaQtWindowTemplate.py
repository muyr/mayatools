# -*- coding: cp936 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################
# 经过 Maya 2013 2014 测试
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    import sip
    sip.setapi("QString",  2)
    sip.setapi("QVariant",  2)
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

# 设置 tr 的编码方式为中文
QTextCodec.setCodecForTr(QTextCodec.codecForName("gbk"))

# 获取 Maya 主窗口
def getMayaMainWindow():
    return QApplication.activeWindow()

#################################
# 修改这里的代码为你定义的窗口类
mayaLibWindow  = QLabel(parent = getMayaMainWindow()) # parent 设置为 Maya 主窗口
mayaLibWindow.setText(mayaLibWindow.tr('<font color = "red", size = 28>测试</font>'))
mayaLibWindow.setObjectName('MayaLibWindow') # 一定要设置
################################

# 若目标窗体了存在，就删除掉
for widget in qApp.allWidgets():
    if widget.objectName() == 'MayaLibWindow': # 此处的 'MayaLibWindow' 改为你 setObjectName 的参数
        widget.close()

mayaLibWindow.setWindowFlags(Qt.Window)
mayaLibWindow.show()