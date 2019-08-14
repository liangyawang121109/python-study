import os
import sys
import json

BASE_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_dir)

def login(func):
    def authca(*args,**kwargs):
        username = input("请输入您的账户：")
        password = input("请输入你的密码：")
        with open('auth','r',encoding='utf-8') as f:
            data = json.load(f)
        if username in data:
            if int(password) == int(data[username]):
                print("登录成功")
                func(*args,**kwargs)
            else:
                print("账号或者密码错误")
        else:
            print("你输入的账户不存在")
    return authca


def choose():
    choo = input("输入项目序列号：")
    if int(choo) == 1:
        print("余额查询")
    elif int(choo) == 2:
        print("新用卡取现")
    elif int(choo) == 3:
        print("信用卡还款")
    elif int(choo) == 4:
        print("信用卡取现")




@login
def index():
    print("欢迎来到亚旺银行取款机")
    print("请选择您要进行的项目序列号:")
    projlist = [
            "余额查询",
            "信用卡取现",
            "信用卡还款",
            "账单查询",
    ]
    listnum = [1,2,3,4,5]
    res = zip(listnum,projlist)
    for i in res:
            print(i)
    choose()

#index()
