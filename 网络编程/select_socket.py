import select
import socket
import queue

server = socket.socket()    
server.bind(('localhost',8080))
server.listen()
conn,addr = server.accept()
while True:
    data = conn.recv(1024)
    print(data.decode())
    conn.send(data)