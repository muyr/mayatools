###################################################################
# Author: Mu yanru
# Date    : 2013.07
# Email : muyanru345@163.com
###################################################################
#-*- coding: cp936 -*-

import maya.cmds as mc


###################################################################
# ��ȡ������ѡ�������Ƕ�Ӧ�� Reference �ļ�
###################################################################
def getSelectReferenceFile():
    selectObjs = mc.ls(sl = True)
    result = []
    for obj in selectObjs:
        if mc.referenceQuery(obj, isNodeReferenced = True):
            if not result.count(mc.referenceQuery(obj, filename = True)):
                result.append( mc.referenceQuery(obj, filename = True))
    return result

###################################################################
# ��ȡ���������е� Reference �ļ�
###################################################################
def getAllReferenceFile():
    return mc.file(q = True, reference = True)

###################################################################
# ɾ�������������е� Reference �ļ�
###################################################################
def removeAllReferenceFile():
    for obj in getAllReferenceFile():
        mc.file(obj, removeReference = True)

###################################################################
# reload ���������е� Reference �ļ�
###################################################################
def reloadAllReferenceFile():
    for obj in getAllReferenceFile():
        mc.file(obj, loadReference = True)

###################################################################
# unload ���������е� Reference �ļ�
###################################################################
def unloadAllReferenceFile():
    for obj in getAllReferenceFile():
        mc.file(obj, unloadReference = True)

###################################################################
# import ���������е� Reference �ļ�
###################################################################
def importAllReferenceFile():
    for obj in getAllReferenceFile():
        mc.file(obj, importReference = True)

###################################################################
# ɾ����������ѡ�е� Reference �ļ�
###################################################################
def removeSelReferenceFile():
    for obj in getSelectReferenceFile():
        mc.file(obj, removeReference = True)

###################################################################
# reload ������ѡ�е� Reference �ļ�
###################################################################
def reloadSelReferenceFile():
    for obj in getSelectReferenceFile():
        mc.file(obj, loadReference = True)

###################################################################
# unload ������ѡ�е� Reference �ļ�
###################################################################
def unloadSelReferenceFile():
    for obj in getSelectReferenceFile():
        mc.file(obj, unloadReference = True)

###################################################################
# import ������ѡ�е� Reference �ļ�
###################################################################
def importSelReferenceFile():
    for obj in getSelectReferenceFile():
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

