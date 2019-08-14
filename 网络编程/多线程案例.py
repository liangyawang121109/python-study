import threading
import time

class thread(threading.Thread):
    def __init__(self,num):
        super(thread,self).__init__()
        self.num = num

    def run(self):
        print('%s'% self.num)

t1 = thread('t1')
t2 = thread('t2')
t1.start()
t1.join() #如果join 就相当于wait 也就是说将并行改成了串行 等待第一个执行完成才会执行下一个
t2.start()


