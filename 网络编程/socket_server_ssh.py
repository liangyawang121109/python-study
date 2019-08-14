import socket
import os

server = socket.socket()

server.bind(('localhost',8080))
server.listen()
while True:
    conn,addr = server.accept()
    print('new',conn,addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('客户端已断开')
            break
        print('发送指令',data)
        cmd_res = os.popen(data.decode()).read()
        print('send before',len(cmd_res))
        if len(cmd_res) == 0:
            conn.send("send data is 0".encode('utf-8'))
        conn.send(str(len(cmd_res)).encode('utf-8'))
        check = conn.recv(1024)
        print(check.decode())
        conn.send(cmd_res.encode('utf-8'))
        print('send done')
    server.close()