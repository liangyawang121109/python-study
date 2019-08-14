"""
import sys
import os

file = sys.argv[1]
old = sys.argv[2]
new = sys.argv[3]

with open(file,"r",encoding="utf-8") as f,\
    open("test1","w",encoding="utf-8") as f1:
    for i in f:
        if old in i:
            i = i.replace(old,new)
        f1.write(i)

os.remove("test")
os.rename("test1","test")
#以上为python3环境的实现sed替换的代码

"""
"""
#以下为python2环境实现sed替换的代码
#-*- coding:utf-8 -*-
import sys
import os
import io
reload(sys)
sys.setdefaultencoding('utf8')

old = sys.argv[1]
new = sys.argv[2]

with io.open("test","r",encoding='utf-8') as f,\
    io.open("test1","w",encoding='utf-8') as f1:
    for i in f:
        if old in i:
            i = i.replace(old,new)
        f1.write(i)

os.remove("test")
os.rename("test1","test")
"""