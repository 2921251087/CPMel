#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/11/10 22:28
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import shutil
import CPCLI.build as build
import CPCLI.group as group
# import CPCLI.build,CPCLI.group as build
#
root = u"D:/Development/MAYA/CPMEL/CPMEL"
try:
    shutil.rmtree(root + u"/build")
except:
    pass

class release(object):
    comms = True
    deletedoc = True
    deletezeroline = True
build.main(root + u"/src",
           root + u"/moves.txt",
           root + u"/build/release",
           release)
class debug(object):
    comms = True
    deletedoc = False
    deletezeroline = False
build.main(root + u"/src",
           root + u"/moves.txt",
           root + u"/build/debug",
           debug)
# build.main(root + u"/debug",
#            root + u"/moves.txt",
#            root + u"/build/src")
# group.build(root + u"/build/src",
#             root + u"/build/plug",
#             u"CPTest")
# shutil.rmtree(r"D:\Development\MAYA\build\cpweidgets-v-0.03")
# group.build(r"D:\Development\MAYA\cpweidgets-v-0.03",
#             r"D:\Development\MAYA\build\cpweidgets-v-0.03",
#             u"weidgets")

