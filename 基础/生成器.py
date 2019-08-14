#列表生成式
"""
a = [i*2 for i in range(10)]
print(a)
"""
#通过列表生成式 我们可以直接创建一个列表 但是 受到内存限制 列表容量肯定是有限的 而且 创建一个包含一百万个元素的列表
#不仅占用很大的存储空间 如果我们仅仅需要访问前面几个元素 那后面绝大多数的元素占用空间就浪费了
#所以 如果列表元素可以按照某种算法推算出来 我们是否可以在循环的过程中不断推算出后续的元素呢 这样就不必创建完整的
#list 从而节省大量的空间 在python中 这种一边循环一遍计算的机制叫做生成器 generator
#生成器 只有在调用时才会生成相应的数据
"""
b = (i*2 for i in range(10))
for i in range(3):
   print(b.__next__()) #next只记录当前的一个位置 下次执行就记录下一个位置
"""
    #生成器只能访问当前位置的下一个数据而不能返回到上一个数据 它只记录当前的数据 不记录上一个位置 也不知道下一个位置
    #只是调用的时候生成下一个数据

#用函数 做一个生成器
"""
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield (b) #使用yield 使这个函数成为生成器
        a,b = b, a+b
        n = n+1
    return "------------done------------" #此返回值是如果取的数据超出生成器有的数据返回异常时返回的一个数据
                    #但是如果用for循环这个值不会返回 return的值什么 那么异常信息就是什么



#for i in range(11): #使用for循环加next然后查询想要的数据
#    print(c.__next__()) #如果一个生成器里只有10个数据 那么最多就能拿取10次数据 如果超出了就会报错 抛出一个异常

#那么这个时候就需要做一个异常抓取机制了


c = fib(10)
g = fib(6) #赋值
while True: #它会生成一个死循环 不停地从生成器g里边执行next 直到抛出异常后 抓取异常
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('generator return value:',e.value)
        break
"""
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())
# print(c.__next__())


