###################################################################
# Author: Mu yanru
# Date    : 2013.07
# Email : muyanru345@163.com
###################################################################
#-*- coding: cp936 -*-

import maya.cmds as mc

###################################################################
# 删除掉场景中所有的 Reference 文件
###################################################################
def removeAllReferenceFile():
    referenceFileList = mc.file(q = True, r = True)
    for obj in referenceFileList:
        mc.file(obj, rr = True)

###################################################################
# reload 场景中所有的 Reference 文件
###################################################################
def reloadAllReferenceFile():
    referenceFileList = mc.file(q = True, r = True)
    for obj in referenceFileList:
        mc.file(obj, loadReference = True)

###################################################################
# unload 场景中所有的 Reference 文件
###################################################################
def unloadAllReferenceFile():
    referenceFileList = mc.file(q = True, r = True)
    for obj in referenceFileList:
        mc.file(obj, unloadReference = True)

###################################################################
# import 场景中所有的 Reference 文件
###################################################################
def importAllReferenceFile():
    referenceFileList = mc.file(q = True, r = True)
    for obj in referenceFileList:
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

