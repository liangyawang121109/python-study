import threading,time

semaphore = threading.BoundedSemaphore(5)

def run(n):
    semaphore.acquire()
    time.sleep(1)
    print( 'run the thread',n)
    semaphore.release()

for i in range(50):
    t = threading.Thread(target=run,args=(i,))
    t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print('all threads done')
