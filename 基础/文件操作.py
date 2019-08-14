#f = open("liangyawang","r",encoding="utf-8")
#data = f.read() #读一个文件 r 读文件 默认不写就是 r 但是这个方法只能是读 不可写 一次性读出文件的所有内容 读完以后光标移动到文件最后
#print(data)

"""
f = open("liangjing","w",encoding="utf-8") #对文件进行写操作 它会创建一个新的文件 如果已有这个文件会进行清空 然后重新写入
f.write("不要放弃了  我们不是没有余地的\n") #如果不加换行符 两次写将写成一行
f.write("我是爱你的 但是每个人绝对不是完美的")
f.close
"""
"""
f = open("liangjing","a",encoding="utf-8") #追加到文件末尾 不会清空原有内容  不可读文件
f.write("\n我是个恨不得成为你肚子里蛔虫的人 ") #如果不加\n 会将数据写成一行
"""
"""
f = open("liangjing","r",encoding="utf-8")
#print(f.readline())
#print(f.readline())
#print(f.readline()) #以上三次读 读出了文件的前三行 readline 对文件进行一行一行读取
#简写打印前三行操作
for i in range(3):
    print(f.readline())
"""
"""
f = open("liangjing","r",encoding="utf-8")
#print(f.readlines()) #以列表的形式读出文件的所有行

for line in f.readlines():
    print(line.strip()) #循环读出文件的所有行 默认会有换行符 去掉它
"""
"""
f = open("liangjing","r",encoding="utf-8")
for index,line in enumerate(f.readlines()): #这种读法 如果是大文件可能会将内存撑爆 因为它保存了每一行的数据在内存里
    if index == 3: #如果到第四行就不打印 跳过它 
        continue
    print(line.strip())
"""
"""
f = open("liangjing","r",encoding="utf-8")
for line in f:
    print(line) #这个也是一行一行的读出文件 但是它只保存一行的数据在内存里 效率最高 常用 他不是以列表的方式读出数据
"""
"""
count = 0
f = open("liangjing","r",encoding="utf-8")
for line in f:
    count+=1
    if count == 3: #因为它的保存数据的方式不再是列表 所以我们无法取出他的下表 所以在此添加一个计数器 每读一行加1 当读到第三行跳过
        continue
    print(line.strip())
"""
"""
f = open("liangjing","r",encoding="utf-8")
print(f.tell()) #打印出光标的位置 他的计数方式是按字符计数
f.readline()
print(f.tell())
f.seek(0) #将光标移动到起始位置
"""

"""
f = open("liangjing","r",encoding="utf-8")
print(f.encoding) #打印文件的编码
print(f.fileno()) #返回文件句柄在内存的编号
print(f.name) #打印正在读的文件名
print(f.isatty()) #判断是否是一个终端设备 返回False True
print(f.seekable())#判断文件光标是否可移动 如果可以返回True 如果不能返回False
print(f.readable()) #判断文件是否可读
print(f.writable()) #判断文件是否可写
"""
"""
f = open("liangjing1","w",encoding="utf-8")
f.write("我爱你 京京")
print(f.flush()) #刷新 默认是等缓存满了以后再刷新到硬盘 而这个是强制刷新到硬盘 保证数据实时持久存储 不会丢失
"""
"""
f = open("liangjing1","r+",encoding="utf-8") #读写 需要有次文件 才可以对文件既可以进行读操作 也可以写操作 写入时直接追加到文件末尾
"""
"""
f = open("liangjing1","w+",encoding="utf-8") #写读 
"""
"""
f = open("liangjing2","wb") #将数据以二进制的方式传递并写入文件里
f.write("京京 我爱你".encode())
f.close()
"""
"""
with open("testlog","a+",encoding="utf-8") as f: #以追加的方式对文件进行写入 w是覆盖原来的 a+ 是追加
    f.write("action is success\n")
"""

