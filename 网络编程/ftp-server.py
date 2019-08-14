import socket
import os
import time

server = socket.socket()
server.bind(('localhost',8080))
server.listen()

while True:
    conn,addr = server.accept()
    while True:
        data = conn.recv(1024).decode().split()
        action,filename = data
        if not data:
            print('客户端连接已断开')
        if str(action).startswith('get'):
            if os.path.exists(filename):
                size = os.stat(filename).st_size
                conn.send(size)
                with open(filename,rb) as f:
                    for line in f:
                        server.send(line.encode())
            else:
                print(filename,'文件不存在')
        elif str(action).startswith('post'):
            print(action,filename)

        print('send ---- done')
    conn.close()

