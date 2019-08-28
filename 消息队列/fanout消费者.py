import pika

credentials = pika.PlainCredentials('admin','121109')
parameters = pika.ConnectionParameters(
    host='172.16.1.218',
    credentials = credentials,
    virtual_host='/test'
)
connection = pika.BlockingConnection(parameters) #建立socket连接 连接至rabbitmq个通信频道
channel = connection.channel()

res = channel.queue_declare(exclusive=True)

queue_name = res.method.queue

channel.queue_bind(exchange='logs',queue=queue_name)

def callback(ch,method,properties,body):
    print('recv%s'%body)

channel.basic_consume(#消费消息
                      callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()