#装饰器 本质就是一个函数 用来装饰其他函数 为其他函数添加附加功能
#原则：
    #1. 不能修改被装饰的函数的源代码
    #2. 不能修改被装饰的函数的调用方式

#写一个简单装饰器
"""
#不可传参数的 装饰器

import time

def timmer(func): #1. 调用函数
    def timfun(): #2. 执行此函数
        start_time = time.time() #3. 执行时间统计
        func() #4. 执行当参数传递进来的函数
        stop_time = time.time() #4. 完成时间统计
        print("end time is %s"%(start_time - stop_time)) #5. 打印函数执行时间
    return timfun #6. timmer函数 执行完以后返回值为 嵌套函数的内存地址
"""
#然后给要被装饰的函数赋值
"""
@timmer #就等同于 test1 = timmer(test1)
def test1():
    time.sleep(3)
    print("test1 end")

#test1()
#test1 = timmer(test1) #这个赋值的过程 就完成了函数不被修改源代码的情况下实现增加新功能
test1()               #而 这个赋值有一个语法糖得语法是这么写的 @timmer
"""

"""
#定义一个 既可以传参数 也可以不传参数 或者传递过个参数的装饰器
import time

def timmer(func):
    def timfunc(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time =time.time()
        print("end time is %s"%(start_time - stop_time))
    return timfunc

# @timmer
# def test1(name):
#     time.sleep(1)
#     print(name)
#
# test1("梁亚旺")

@timmer
def test2(name,age):
    time.sleep(1)
    print(name,age)

test2("liangyawang",12)
"""
