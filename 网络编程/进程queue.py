from multiprocessing import Queue,Process

def f(q):
    q.put('test')
    q.put('tes1')
if __name__ == "__main__":
    q = Queue()
    for i in range(1):
        p = Process(target=f,args=(q,))
        p.start()
        print(q.get())
        p.join()


