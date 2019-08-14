import queue

'''
q =queue.Queue()
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())
#print(q.get(timeout=1)) #如果没有队列数据了 那么等待一秒抛出异常
#print(q.get_nowait()) #如果队列里没有数据了 直接抛出异常
if q.qsize() == 0: #判断如果队列里的数据等于0了那么就直接打印没有数据
    print('no data')
    
'''
'''

q = queue.LifoQueue() #后进去的先被取出来
q.put(1)
q.put(2)
q.put(3)
print(q.get())
print(q.get())
print(q.get())
'''
'''

q = queue.PriorityQueue() #按照字典定义的优先级进行取出数据 如果是字母按照字母的位置 如果数字按照数字大小
q.put((1,'liangyanwang'))
q.put((3,'liangjing'))
q.put((0,'love'))
print(q.get_nowait())
print(q.get_nowait())
print(q.get_nowait())
'''

q = queue.Queue(maxsize=3) #设置实例化的队列里最多只能存放三个数据