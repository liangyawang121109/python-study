import socket

client = socket.socket()
client.connect(('localhost',8080))
while True:
    cmd = input('>>>').strip()
    if len(cmd) == 0: continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024) #接收服务器端发送数据的大小
    print(cmd_res_size.decode())
    client.send('我已准备接收 就绪'.encode())

    received_size = 0
    while received_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        received_size += len(data)
        print(data.decode())
    print(received_size)

client.close()


# cmd_res = client.recv(1024)  接收数据量最大为1024 如果本次发送的数据量超出1024 那么超出的部分就会被存在缓存区
#等待下次调用时返回 那么下次调用输出的值就会被挤到再下一次 这样就会数据错乱 输入的指令和想要的数据牛头不对马尾
