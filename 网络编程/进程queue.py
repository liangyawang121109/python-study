from multiprocessing import Queue,Process

def f(q):
    q.put('test')

if __name__ == "__main__":
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()


