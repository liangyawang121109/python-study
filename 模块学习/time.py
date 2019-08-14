
###time模块
import time 
"""
# 在python中通常用这几种方式来表示时间：
#    1. 时间戳
#    2. 格式化的时间字符串
#    3. 元祖 共九个元素
"""
"""
#获取时间戳
print(time.time()) #这个方法获取到得数字单位是秒 而这个时间是从1970年到现在的时间总计
#让程序睡几秒
time.sleep(2) #睡两秒
#将时间转换为标准时间
time.gmtime() #不传入秒数默认将本地当时的时间传入 然后转换为标准时区的时间的元祖
#当前时区的时间
time.localtime() #将时间戳转换成本地时间的元祖
"""
"""
#将时间取出来
x = time.localtime()
print(x.tm_year) #取出是哪一年
"""
"""
#将结构化的元祖的时间转换成时间戳
time.mktime() #将结构化的时间元祖传入以后转换成时间戳的秒
"""
"""
#将元祖后的时间格式化输出
x = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",x))
"""
"""
#将格式化的时间准换成元祖
time.strptime("2019-06-17 14:15:19","%Y-%m-%d %H:%M:%S")#传入格式化后的时间以及对应的格式转换成元祖
"""
"""
#将元祖格式的时间转换成格式化的
print(time.asctime(time.localtime()))
"""
"""
#将时间戳转换成格式化的
print(time.ctime()) #传入的参数为秒 如果不传就默认传入当前的时间戳
"""
###datetime模块
import datetime
"""
#获取当前时间
print(datetime.datetime.now())
"""
"""
#获取多少天以前的时间
print(datetime.datetime.now()+datetime.timedelta(3)) #获取未来三天的时间
print(datetime.datetime.now()+datetime.timedelta(-3)) #获取三天前的时间
print(datetime.datetime.now()+datetime.timedelta(hours=3)) #当前时间的未来三个小时
print(datetime.datetime.now()+datetime.timedelta(hours=-3)) #当前时间的前三个小时
print(datetime.datetime.now()+datetime.timedelta(minutes=30)) #当前时间的未来三十分钟
"""