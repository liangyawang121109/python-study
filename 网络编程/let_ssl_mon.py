import sys
import ssl
import socket
import time
from datetime import datetime

def info():
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname='imgcnd1.migang.com',)
    conn.settimeout(3.0)
    conn.connect(('imgcdn1.migang.com',443))
    ssl_info = conn.getpeercert()
    return ssl_info
format_time = datetime.strptime(info()['notAfter'], r'%b %d %H:%M:%S %Y %Z')
notbefore = datetime.strptime(info()['notBefore'], r'%b %d %H:%M:%S %Y %Z')
end_days = format_time - datetime.now()

print('有效期至：%s'%format_time)
print('颁发时间为：%s'%notbefore)

print('当前剩余有效天数为：%s'%end_days.days)

