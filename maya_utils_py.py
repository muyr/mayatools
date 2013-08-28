###################################################################
# Author: Mu yanru
# Date    : 2013.07
# Email : muyanru345@163.com
###################################################################
#-*- coding: cp936 -*-

import maya.cmds as mc


###################################################################
# 获取场景中选中物体们对应的 Reference 文件
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
# 获取场景中所有的 Reference 文件
###################################################################
def getAllReferenceFile():
    return mc.file(q = True, reference = True)

###################################################################
# 删除掉场景中所有的 Reference 文件
###################################################################
def removeAllReferenceFile():
    for obj in getAllReferenceFile():
        mc.file(obj, removeReference = True)

###################################################################
# reload 场景中所有的 Reference 文件
###################################################################
def reloadAllReferenceFile():
    for obj in getAllReferenceFile():
        mc.file(obj, loadReference = True)

###################################################################
# unload 场景中所有的 Reference 文件
###################################################################
def unloadAllReferenceFile():
    for obj in getAllReferenceFile():
        mc.file(obj, unloadReference = True)

###################################################################
# import 场景中所有的 Reference 文件
###################################################################
def importAllReferenceFile():
    for obj in getAllReferenceFile():
        mc.file(obj, importReference = True)

###################################################################
# 删除掉场景中选中的 Reference 文件
###################################################################
def removeSelReferenceFile():
    for obj in getSelectReferenceFile():
        mc.file(obj, removeReference = True)

###################################################################
# reload 场景中选中的 Reference 文件
###################################################################
def reloadSelReferenceFile():
    for obj in getSelectReferenceFile():
        mc.file(obj, loadReference = True)

###################################################################
# unload 场景中选中的 Reference 文件
###################################################################
def unloadSelReferenceFile():
    for obj in getSelectReferenceFile():
        mc.file(obj, unloadReference = True)

###################################################################
# import 场景中选中的 Reference 文件
###################################################################
def importSelReferenceFile():
    for obj in getSelectReferenceFile():
        mc.file(obj, importReference = True)

###################################################################
# MEL 由于不支持递归，所以它特别提供了 rootOf 命令，来得到给定物体最上面的组
# 而 rootOf 命令没有 python 版本，估计是觉得 python 用户可以自行搞定
# 以下是 python 版本的 rootOf
###################################################################
def rootOf(obj):
    p = mc.listRelatives(obj, parent = 1)
    if p: 
        return getRootOf(p[0])
    else: 
        return obj

