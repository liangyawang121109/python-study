import threading
import time

def run(n):
    print('tasck',n,threading.current_thread(),threading.active_count())
    time.sleep(2)
t1 = threading.Thread(target=run,args=('t1',))
t2 = threading.Thread(target=run,args=('t2',))

# t1.start()
# t2.start() #并发运行
#
# run(t1)
# run(t2)

start_time = time.time()
res = []

for i in range(50):
    t = threading.Thread(target=run,args=(i,))
    t.setDaemon(True)  #将当前现成设置为守护线程
    t.start()
    res.append(t)
print(threading.active_count())
for  r in res:
    r.join()

print('run time is ',time.time() - start_time)

print('run is done ',threading.current_thread())