#判断一个对象是不是可迭代对象
"""
from collections import Iterable

print(isinstance([],Iterable)) #判断列表是不是一个可迭代对象
"""
#可以被next()函数调用 并且不断返回下一个值的对象统称为迭代器 Iterator

#判断是不是一个迭代器
"""
from collections import Iterator

print(isinstance((x for x in range(5)), Iterator)) #生成器可以被next调用 那么它自然就是返回结果为 True
"""
#生成器都是Iterator对象 但是list dict str虽然是可迭代对象 却不是迭代器
#可以使用 iter() 函数 将list dict str等可迭代对象变成迭代器

from collections import Iterable
from collections import Iterator

li = [1,2,3]
print(isinstance(li, Iterable)) #判断li这个列表是不是一个可迭代对象
print(isinstance(li, Iterator)) #判断li这个列表是不是一个迭代器
print(isinstance(iter(li),Iterator)) #使用iter函数将列表转换以后 在看判断结果
