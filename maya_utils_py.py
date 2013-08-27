###################################################################
# Author: Mu yanru
# Date    : 2013.07
# Email : muyanru345@163.com
###################################################################
#-*- coding: cp936 -*-

import maya.cmds as mc

###################################################################
# ɾ�������������е� Reference �ļ�
###################################################################
def removeAllReferenceFile():
    referenceFileList = mc.file(q = True, r = True)
    for obj in referenceFileList:
        mc.file(obj, rr = True)

###################################################################
# reload ���������е� Reference �ļ�
###################################################################
def reloadAllReferenceFile():
    referenceFileList = mc.file(q = True, r = True)
    for obj in referenceFileList:
        mc.file(obj, loadReference = True)

###################################################################
# unload ���������е� Reference �ļ�
###################################################################
def unloadAllReferenceFile():
    referenceFileList = mc.file(q = True, r = True)
    for obj in referenceFileList:
        mc.file(obj, unloadReference = True)

###################################################################
# import ���������е� Reference �ļ�
###################################################################
def importAllReferenceFile():
    referenceFileList = mc.file(q = True, r = True)
    for obj in referenceFileList:
        mc.file(obj, importReference = True)

###################################################################
# MEL ���ڲ�֧�ֵݹ飬�������ر��ṩ�� rootOf ������õ������������������
# �� rootOf ����û�� python �汾�������Ǿ��� python �û��������и㶨
# ������ python �汾�� rootOf
###################################################################
def rootOf(obj):
    p = mc.listRelatives(obj, parent = 1)
    if p: 
        return getRootOf(p[0])
    else: 
        return obj

