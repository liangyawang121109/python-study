"""
服务端
地址簇：
    AF.INET   IPV4
    AF.INET6  IPV6
    AF.UNIX   local
协议类型：
    socket.SOCK_STREAM  tcp/ip  (默认)
    socket.SOCK_DGRAM   Udp
    socket.SOCK_RAM  可伪造ip地址头
    server = server.socket.socket()

"""
import socket

server = socket.socket() #声明类型  第一步
server.bind(('localhost',6969)) #绑定要监听的端口  第二步 ip地址和端口
server.listen() #监听  第三步 开始监听
while True:
    conn,addr = server.accept() #等待被访问 conn就是客户端连过来而在服务端为其生成的一个链接实例  阻塞并等待
#print(conn,addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data)
        conn.send(b'hahahahahahaha')
#           server.close()
#可不断的接收被访问 但是同时只能同时接收一个
