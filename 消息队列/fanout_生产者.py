import pika
import sys

credentials = pika.PlainCredentials('admin','121109')
parameters = pika.ConnectionParameters(
    host='172.16.1.218',
    credentials = credentials,
    virtual_host='/test'
)
connection = pika.BlockingConnection(parameters) #建立socket连接 连接至rabbitmq个通信频道
channel = connection.channel() #声明一个管道
#fanout 所有绑定到此exchange的queue都可以接收消息

channel.exchange_declare(exchange='logs',exchange_type='fanout') #  写一个exchange 注明类型 消息转化

#messages = ''.join(sys.argv[1:]) or "info hello world"
messages = "info hello world"
channel.basic_publish(exchange='logs',
                      routing_key='', #现在是广播状态 所以之前也没有声明单独的queue 这里也不需要写单独的queue
                      body=messages) #消息主题就是hello world

print('send',messages)
connection.close() #关闭队列

#6章