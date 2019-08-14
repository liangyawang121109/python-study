import socket
#python3数据发送只能发bytes类型
client = socket.socket() #声明socket类型 同时生成socket链接对象  第一步 实例化一个socket
client.connect(('localhost',6969))  #第二步 连接要访问的ip 端口
client.send(b"hello world") #第三步  发送数据
data = client.recv(1024) #
print(data)
client.close()

