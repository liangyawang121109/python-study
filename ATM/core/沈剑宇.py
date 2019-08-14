import os

def mebaded():
    name = input("请输入您要注册的账户")
    password = input("请输入你要注册的密码")
    def mebadd(name,password):
        """人员注册添加"""
        import json


        with open('auth.txt','r', encoding="utf-8") as f:
            line = f.readline()
            b = eval(line)
            b[name] = password
            jsObj = json.dumps(b)
            fileObject = open('auth.txt', 'w', encoding="utf-8")
            fileObject.write(jsObj)
            fileObject.close()

        print("您的账户已经注册成功")
    mebadd(name,password)

mebaded()
