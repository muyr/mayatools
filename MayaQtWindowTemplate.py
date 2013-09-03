# -*- coding: cp936 -*-
###################################################################
# Author: Mu yanru
# Date  : 2013.09
# Email : muyanru345@163.com
###################################################################
# ���� Maya 2013 2014 ����
try:
    from PySide.QtCore import *
    from PySide.QtGui import *
except ImportError:
    import sip
    sip.setapi("QString",  2)
    sip.setapi("QVariant",  2)
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *

# ���� tr �ı��뷽ʽΪ����
QTextCodec.setCodecForTr(QTextCodec.codecForName("gbk"))

# ��ȡ Maya ������
def getMayaMainWindow():
    return QApplication.activeWindow()

#################################
# �޸�����Ĵ���Ϊ�㶨��Ĵ�����
mayaLibWindow  = QLabel(parent = getMayaMainWindow()) # parent ����Ϊ Maya ������
mayaLibWindow.setText(mayaLibWindow.tr('<font color = "red", size = 28>����</font>'))
mayaLibWindow.setObjectName('MayaLibWindow') # һ��Ҫ����
################################

# ��Ŀ�괰���˴��ڣ���ɾ����
for widget in qApp.allWidgets():
    if widget.objectName() == 'MayaLibWindow': # �˴��� 'MayaLibWindow' ��Ϊ�� setObjectName �Ĳ���
        widget.close()

mayaLibWindow.setWindowFlags(Qt.Window)
mayaLibWindow.show()