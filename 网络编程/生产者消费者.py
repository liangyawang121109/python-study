import threading,time,queue

q = queue.Queue()
def producer(name):
    for i in range(10):
        q.put('包子%s被%s做好了'%(i,name))

def consumer(name):
    while q.qsize() > 0:
        i = q.get_nowait()
        print('%s is eat%s'%(name,i))
    else:
        print('包子被%s吃完了'%name)

p = threading.Thread(target=producer,args=('liangyawang',))

p1 = threading.Thread(target=consumer,args=('liangjing',))

p.start()
p1.start()