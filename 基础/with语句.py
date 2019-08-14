with open("test","r",encoding="utf-8") as f: #打开文件并循环读出文件内容 自动关闭文件
    for i in f:
        print(i)

with open("test","r",encoding="utf-8") as f,\
        open("test1","w",encoding="utf-8") as f2:
        for i in f:
            f2.write(i) #with可支持同时打开多个文件进行读取或读写 例如读取此文件然后将此文件内容写入到另一个