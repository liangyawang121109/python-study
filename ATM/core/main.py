import os
import sys
from os import listdir

BASE_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_dir = 'D:/python学习 project/ATM/bin'

def register():
    name = input("请输入您要注册的账户")
    password = input("请输入你要注册的密码")
    def mebadd(name,password):
        """人员注册添加"""
        import json
        if os.path.exists("auth"):
            with open('auth','r', encoding="utf-8") as f:
                with open('auth1','w',encoding='utf-8') as f2:
                    line = f.readline()
                    b = eval(line)
                    b[name] = password
                    json.dump(b,f2)
                    print("您的账户已经注册成功")
            os.remove('auth')
            os.rename('auth1', 'auth')
        else:
            with open('auth', 'w', encoding="utf-8") as f:
                memb = {

                }
                memb[name] = password
                json.dump(memb, f)
    mebadd(name,password)

#register()

