import time

#next 调用yield的时候 只是对yield唤醒 调用 而不传值
#send 调用yield的时候 不仅对yield唤醒 调用而且调用的同时进行传值

def consumer(name):
    print("%s 准备吃包子了" % name)
    while True:
        baozi = yield

        print("%s 包子来了，包子被 %s 吃了" %(baozi,name))

c = consumer("liangyawang ")
c2 = consumer("liangjing")
# c.__next__()
# c.send("韭菜")
# c.__next__()
# c.send("白菜")

baozi_list = ['韭菜','白菜','茴香','香菇']
def produc():

        c.__next__()
        c2.__next__()
        for i in baozi_list:
            c.send(i)
            c2.send(i)


produc()

# c.__next__()
# c.__next__()
