import urllib
from urllib.request import urlopen
import gevent
import time
from gevent import monkey

monkey.patch_all() #添加这个补丁可让gevent识别urllib的io操作 而让gevent发生io自动切换

def f(url):
    print('get %s'%url)
    resq = urllib.request.urlopen(url)
    data = resq.read()
  #  with open('test','wb') as f:
   #     f.write(data)
    print(len(data),url)

url = ['http://www.cnblogs.com/alex3714/articles/5248247.html','https://k.i4t.com/kubernetes.html','https://www.github.com']
#"""
start_time1 = time.time()
for i in url:
    f(i)
end_time1 = time.time() - start_time1

print(end_time1)
#计算串行爬数据的时间消耗
#"""
#"""
start = time.time()
gevent.joinall(
    [
        gevent.spawn(f,'http://www.cnblogs.com/alex3714/articles/5248247.html'),
        gevent.spawn(f,'https://www.github.com'),
        gevent.spawn(f,'https://k.i4t.com/kubernetes.html'),
    ]
)
end = time.time() - start
print(end)
#计算gevent并发执行爬数据的时间消耗
#gevent默认检测不到urllib的io操作 所以gevent不会发生io自动切换 所以就相当于是执行了串行爬数据 消耗的时间可想而知跟串行几乎一样
#所以此时需要添加一个补丁来让gevent识别urllib的io操作 这个补丁是monkey
#"""
#可以看到打上补丁以后 gevent协程爬虫明显比串行爬虫消耗时间较短 提高效率

