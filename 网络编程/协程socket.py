import gevent
from urllib.request import urlopen
import time
import socket

from gevent import monkey

monkey.patch_all()

def url_server():
    s = socket.socket()
    s.bind(('0.0.0.0',81))
    s.listen()
    while True:
        conn,addr = s.accept()
        gevent.spawn(handler_request,conn)

def handler_request(cli):
    try:
        while True:
            data = cli.recv(1024)
            if not data:
                break
            print(data)
            cli.send(data)
    except Exception as ex:
        print(ex)
    finally:
        cli.close()

if __name__ == '__main__':
    url_server()