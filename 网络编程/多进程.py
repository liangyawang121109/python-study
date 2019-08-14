import multiprocessing
import time
import os
'''
def run(name):
    print('hello',name)

if __name__ == '__main__':
    p = multiprocessing.Process(target=run,args=('yawang',))
    p.start()
'''
'''
def info(name):
    print(name)
    print(os.getppid())
    print(os.getpid())

def run():
    info('get pid and ppid') #打印出子进程的pid和父id

if __name__ == '__main__':
    info('main is pid and ppid') #打印出主进程的pid和父id
    p = multiprocessing.Process(target=run,)
    p.start()
'''
