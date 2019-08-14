"""
#面向对象： 类 class
#面向过程： 过程 def
#函数式编程： 函数 def
"""

"""定义一个函数"""
#def funcl():
#    """函数定义"""
#   print("in the funcl")
#   return 0


"""定义一个过程"""
#def funcl1 ():
#    """面向过程的定义"""
#    print("in the funcl1")
#函数和面向过程两者都可以被调用 他们之间的区别就是 面向过程的定义实际上就是没有返回值的函数

#x = funcl()
#y = funcl1()
#print(x,y)

"""函数的用法"""
#假设我们有三个函数 然后每一个函数执行都需要往日志里写一个东西 意思就是需要写日志的这个功能
#那么我们就可以将写这个功能定义为一个函数 然后在其余的三个函数里进行调用
"""函数优点"""
#代码重用
#保持一致性
#可扩展性

import time

def logwrite ():
    """定义一个日志写入的功能"""
    """日志写入时 加入时间戳"""
    time_format = "%Y-%m-%d %X" #给时间戳定义一个格式  年-月-日 时分秒
    time_output = time.strftime(time_format)  #引用上边的这个时间格式
    with open("testlog","a+",encoding="utf-8") as f: #此处需要以追加的方式对文件进行写入 w是覆盖原来的 a+ 是追加
        f.write("%s action is success\n" %time_output) #此处加\n是为了让写完一段日志就换行 将每一行日志添加时间戳


def test1():
    """定义一个函数 测试日志写入功能函数"""
    print("in the test1")
    logwrite()

def test2():
    """定义第二个函数 测试日志写入功能函数"""
    print("in the test2")
    logwrite()

def tset3():
    """定义第三个函数 测试日志写入功能函数"""
    print("in the test3")
    logwrite()


test1()
test2()
tset3()