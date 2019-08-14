"""
school = "liangjiabao edu" #全局变量 全局变量在整个程序的执行过程中都可以被访问调用

def change_name(name):
    school = "wenshui edu"
    print("before change",name,school) #当全局变量
    name = "Alex" #局部变量 只在函数里生效 这个函数就是这个变量的作用域
    print("after change",name) #出了函数 如果函数之外有这个变量 那么这个变量就是函数之外的值 如果函数之外
name = "alex"                  #没有这个变量 那么就没有这个变量

change_name(name)
"""
"""
#当全局也有此变量 函数体也有此变量的时候 函数体内的变量是无法改变全局变量的 如果函数体内的变量
#想要改变全局变量 需要做一个申明 如下
school = "liangjiabao edu" #在此处赋值全局变量
def change(name): #定义一个形参
    global school #做声明 全局修改school变量
    school = "wenshui " #修改为另一个值
    print(school) #执行此函数时打印此变量的值

change(1) #因为之前定义了形参 所以随便传一个值进去 执行此函数
print(school) #然后打印全局变量school的值 已经发生了改变
"""
#当全局没有定义某个变量 而函数体内定义了此变量并且申明了全局变量时 如果需要用到此变量
#那么需要在使用之前先调用此函数 如果不先进行调用 先使用此函数体内的变量 那么将会报错
def change():
    global name
    name = "liangyawang"

change() #先调用 赋值全局
print(name)
change() #后调用 报错

#但是 函数体内的变量 不可更改全局的程序变量

#字符串 整数 是不能在函数体内进行全局修改的 如果想修改那么需要做一个全局声明
#但是 列表 字典 集合 类 这些都是可以在函数体内进行全局修改的 元祖不可修改