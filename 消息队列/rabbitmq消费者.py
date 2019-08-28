import pika
import time

credentials = pika.PlainCredentials('admin','121109')
parameters = pika.ConnectionParameters(
   host='172.16.1.218',
    credentials = credentials,
    virtual_host='/test'
)
connection = pika.BlockingConnection(parameters) #建立socket连接 连接至rabbitmq

channel = connection.channel() #声明与生产者同样的管道

channel.queue_declare(queue='hello2',durable=True) #  声明一个queue durable=Truhe 对消息队列数据持久化宕机不丢失数据

def callback(ch,method,properties,body):
    time.sleep(10)
    print('recv body message %s'%body)
    ch.basic_ack(delivery_tag=method.delivery_tag) #当no_ack=false时 如果不添加此确认动作 那么即使消费者处理完消息 它也不会向
    #server确认此消息已经消费 而添加此动作 消费者处理完消息后就会发确认动作 然后server就会删除已经处理过的消息
channel.basic_qos(prefetch_count=1) #消费者端加此参数那么 消费者同时只接受一个消息 如果有一个消息没有处理完 那么就不在接收了
channel.basic_consume(#消费消息
                      callback,  #如果收到消息 就调用callback函数处理消息
                      queue='hello2') #如果此处不加no_ack=True 默认为false

channel.start_consuming() #当它开始的时候 会一直处于接收状态 如果没有消息就等待接收 会一直处于卡在等待状态
