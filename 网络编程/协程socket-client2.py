import socket

cli = socket.socket()
cli.connect(('localhost',81))
while True:
    msg = bytes(input('>>>>>>>'),encoding='utf-8')
    cli.send(msg)
    data = cli.recv(1024)
    print(repr(data))