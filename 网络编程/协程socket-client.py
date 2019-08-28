import socket

cli = socket.socket()
cli.connect(('172.16.1.65',8888))
while True:
    msg = bytes(input('>>>>>>>'),encoding='utf-8')
    cli.send(msg)
    data = cli.recv(1024)
    print(repr(data))