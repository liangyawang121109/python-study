import os
"""
#获取当前的工作目录
print(os.getcwd())

#切换目录
os.chdir("C:/Windows")

#返回当前目录
os.curdir

#返回上一级目录
os.pardir
"""
"""
#递归创建多级目录
os.makedirs(r"C:/a/b")

#删除目录 如果目录为空则递归删除到上级目录 如果上级还是空那么继续递归
os.removedirs(r"C:/a/b")
"""
"""
#创建目录 不能递归创建
os.mkdir(r"D:\a")

#只删除单级空目录 若目录不为空则无法删除
os.rmdir()
"""
"""
#列出某一个目录里边的内容
os.listdir()

#删除一个文件
os.remove()

#重命名
os.rename()
"""
"""
#获取文件、目录的信息
print(os.stat(r"D:\7zxa.dll"))
"""
"""
#输出操作系统特定的路径分隔符
print(os.sep)

#输出当前操作系统特定的终止符
print(os.linesep)

#输出用于分割文件路径的字符串
print(os.pathsep)

#查看当前系统的环境变量
print(os.environ)

#输出代表当前使用系统的字符串
print(os.name)

#执行当前系统的命令
os.system("dir")

#获取某一文件的绝对路径
print(os.path.abspath(__file__))

#将目录与文件分开
os.path.split(r"C:\a\b\a.txt")

#返回path的目录 可以不考虑此路径是否存在
os.path.dirname(r"C:\a\b\a.txt")
"""
"""
#返回path的最后一级 可以不考虑此路径是否存在
os.path.basename(r"C:\a\b\a.txt")

#判断输入的路径是否存在
print(os.path.exists(r"C:\a\b\a.txt"))
"""
"""
#判断是否是绝对路径
print(os.path.isabs(r"C:\a\b\a.txt"))

#判读是不是一个文件
os.path.isfile()

#判断是不是一个目录
os.path.isdir()
"""
#获取path所指向文件或目录的最后的存取时间
print(os.path.getatime())

#获取文件或目录的修改时间
print(os.path.getmtime())

#