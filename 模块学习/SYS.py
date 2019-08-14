import shutil

"""
#将一个文件的内容复制到另一个文件 注意编码
f1 = open('test',encoding='utf-8')
f2 = open('test2','w',encoding='utf-8')
shutil.copyfileobj(f1,f2)
"""
"""
#直接输入文件名即可实现复制文件
shutil.copyfile('test','test2')
"""
"""
#拷贝权限 将源文件的权限拷贝到新文件 而新文件的属主属组是新的
shutil.copymode('test','test2')
"""
"""
#拷贝状态信息
shutil.copystat(src,dst)
"""
"""
#拷贝文件和权限 先复制文件然后复制文件的权限
shutil.copy()
shutil.copy2()
"""
"""
#递归的拷贝文件 输入被递归拷贝的父集目录 然后输入新创建的目录 即可递归拷贝
shutil.copytree()
"""
"""
#递归的去删除目录 无论目录有无内容均可递归删除
shutil.rmtree()
"""
"""
#递归的移动文件
shutil.move()
"""
"""
#创建压缩包并返回文件路径 例如 zip tar
shutil.make_archive("test_shut",'zip','D:\python学习 project\模块学习') #要压缩成什么文件名 压缩类型 被压缩的文件或目录路径
"""
"""
#可单独对文件进行压缩
import zipfile
z = zipfile.ZipFile('modu.zip','w')
z.write('test')
"""