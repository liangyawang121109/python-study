from multiprocessing import Process,Manager
import os
#进程之间的数据共享
def f(d,l):
    d[1] = 'test'
    d[2] = 'test2'
    l.append(os.getpid())



if __name__ == "__main__":
    with Manager() as manager:
        d = manager.dict() #生成一个字典 可在多个进程间共享传递数据
        l = manager.list(range(5))

        p_list = []

        for i in range(10):
            p = Process(target=f,args=(d,l,))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(l)
