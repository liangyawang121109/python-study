import pika

#pika安装 pip instlal pika==0.12 安装0.12版本pika

#当前脚本由于在rabbitmq设置了admin可管理的hosts为/test 所以在此需要添加virtual_hosts
#通过rabbitmqctl list_ueues可查看当前rabbitmq里存在的队列 以及队列里没有被处理的消息数量 如果设定了vhost 需要在后边加参数-p 然后指定vhost
#rabbitmq的数据是存储在内存中的 当运行中发生宕机以后 那么数据也就随之丢失了 所以在此我们需要对数据做持久化 无论是生产者还是消费者都需要添加
#持久化参数
#广播模式 exchange必须精确地知道收到的消息要发给谁 exchange的类型决定怎么处理
#类型如下：
    #fanout 所有绑定到此exchange的queue都可以接收消息
    #direct 通过routingKey和exchange决定的那个唯一的queue可以接收消息
    #topic 所有符合routingKey的routingKey所绑定的queue可以接收消息
credentials = pika.PlainCredentials('admin','121109')
parameters = pika.ConnectionParameters(
    host='172.16.1.218',
    credentials = credentials,
    virtual_host='/test'
)
connection = pika.BlockingConnection(parameters) #建立socket连接 连接至rabbitmq个通信频道
channel = connection.channel() #声明一个管道
channel.queue_declare(queue='hello2',durable=True) #  声明一个queue durable=Truhe 对消息队列持久化宕机时队列不丢失但是不对队列里的数据持久化

channel.basic_publish(exchange='',
                      routing_key='hello2', #将消息发送到hello这个queue里
                      body='hello world', #消息主题就是hello world
                      properties = pika.BasicProperties(
                          delivery_mode= 2 #加此参数就是对队列里的数据也持久化 宕机时 durable持久化了队列 而此参数持久化了队列里的数据
                          #保证了数据不丢失
                      )
                      )
print('sent hello world')
connection.close() #关闭队列
