from multiprocessing import Process,Pool
import time

def foo(i):
    time.sleep(2)
    print('hello',i)
   # return i

def bar(TEST):
    print('回调函数正在执行',TEST)


if __name__ == '__main__': #在windows上运行进程池就需要加这么一句话 否则不能运行
    pool = Pool(5) #允许进程池里同时放入5个进程
    for i in range(10):
       # pool.apply_async(func=foo,args=(i,)) #异步执行 并行执行 必须加在close后边加join等待完成 否则不等进程池完成就关闭进程池了
        #pool.apply(func=foo,args=(i,)) #同步执行 串行执行
        pool.apply_async(func=foo,args=(i,),callback=bar) #callback执行完func的函数任务以后 回调callback的函数 func的函数的return结果将作为callback的函数的参数传递进去

    print('end')
    pool.close()
    pool.join()