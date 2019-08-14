import socket

client = socket.socket()
client.connect(('localhost',8080))
while True:
    request = input('>>>>>>')
    if len(request) == 0:continue
    client.send(request.encode())
    size = client.recv(1025).decode()
    client.send('client端已准备接收'.encode())
    read_size = 0
    while read_size < int(size):
        data = client.recv(1024).decode()
        cli_size = len(data)
        read_size += int(cli_size)
        print(data)
        print('数据传输大小为：', size)
        print('接收数据大小为：',read_size)
client.close()