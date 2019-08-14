import os


f = open("test","r",encoding="utf-8") #首先读取此文件
f_new = open("test2","w",encoding="utf-8") #找一个不存在的文件写入
for i in f: #循环读取源文件的每一行
    if "梁亚旺" in i: #假如这里有我们需要修改的字符
        i = i.replace("梁亚旺","梁京") #那么对它进行替换
    f_new.write(i) #对所有读取第一个文件的内容以及修改后的内容进行写入到一个新的文件
f.close()
f_new.close()
os.remove("test") #使用os模块删掉原来的文件
os.rename("test2","test") #使用os模块将文件名改为源文件的名称