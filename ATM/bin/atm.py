import os
import sys
import json

BASE_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_dir)
from core import main
from core import sign

print('\033[7;31m请选择您要进行的项目\033[1;31;40m')
pro = {
    1:"已有账户登录",
    2:"注册账户"
}

for i in pro.items():
    print(i)

def choose2():
    cho = input("请输入您的项目")
    if int(cho) == 1:
        sign.index()
    elif int(cho) ==2:
        main.register()

choose2()


