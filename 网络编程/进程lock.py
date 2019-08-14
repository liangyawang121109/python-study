from multiprocessing import Lock,Process

def f(l,i):
    l.acquire()
    print(i)
    l.release()

if __name__ == "__main__":
    lock = Lock()
    for num in range(10):
        p = Process(target=f,args=(lock,num,))
        p.start()
