#abs() 取绝对值
"""
print(abs(1))
print(abs(-1))
"""
#all() 判断一个可迭代对象里的元素都为真即返回True
"""
print(all([0,-1,3])) #只要不是0都是true 那么这个判断就是false 如果是空那么也返回true
"""
#any() 判断一个可迭代对象里的元素任意一个为真 那就返回True 如果是空那就返回false
"""
print(any([0,-1,3])) #与all真好相对相反一些 
"""
#bin() 十进制转二进制
"""
print(bin(1)) 返回 0b1
print(bin(2)) 返回 0b10
print(bin(255)) 返回 0b10
"""

#bool() 判断真假
"""
print(bool(1)) #返回为真
print(bool(0)) #返回为假

print(bool([])) #空返回假
print(bool([1])) #有数据返回真
"""
#bytearray() 将字符串变成列表的格式 通过ascii码的排序可以进行修改
"""
a = bytearray("abde",encoding="utf-8")
a[0] = 100 #也就是 将字符串变成列表的形式 那么a[0]就表示a这值里边abde的第一个字母 然后通过它在ascii的排序序列号将其修改
print(a)
"""
#callable #判断一个东西是否可以被调用 例如函数可以调用 而列表就不可以
"""
def test1():
    pass
a = []
print(callable(test1)) #test1为函数 所以它是可以调用的 返回true
print(callable(a)) #a是一个列表 他不可以调用
"""
#chr 将数字对应的ascii表中的字符打印出来
"""
print(chr(98))
print(chr(97))
"""
#ord 输入字符 然后返回字符所对应的ascii表中的位置
"""
print(ord('a'))
print(ord('b'))
"""
#classmethod

#compile 将字符串编译成可执行的代码
"""
c = "for i in range(10):print(i)"
#compile('c','','exec')
exec(c) #代码成为字符串以后 可以使用exec直接将字符串赋的值进行执行 不用compile编译也行
#可实现动态导入代码的过程
"""
#dir 查看一个对象得内部可以使用方法

#divmod 返回两个数相除的结果 并返回余数
"""
print(divmod(5,2))
"""
#enumerate #可同时列出一个可遍历数据对象的数据和下标
"""
li = ['a','b','c']
print(list(enumerate(li)))
"""
#eval 将字符串变成字典
"""
print(eval('1+2'))
"""
"""
c = lambda n:3 if n<4 else n #三元运算 如果传递参数是n的值小于4那么就是3 如果n大于4那么就是传递进来的值

print(c(1))
"""
#匿名函数结合filter
"""
res = filter(lambda n:n>5,range(10)) #在10以内的数据里取出大于5的数据 过滤匿名函数规则内的数据并生成迭代
for i in res:
    print(i)

"""
#map #对传入的每一个值进行处理 按照匿名函数内的规则
"""
res= map(lambda n:n*n,range(10)) #
for i in res:
    print(i)
"""
#reduce 将输入的值依次进行计算 累加或其他
"""
import functools
res = functools.reduce(lambda x,y:x+y,range(10))
print(res)
"""

#frozenset 将集合变成一个不可变的集合 冻结结合 让它不能被修改 删除等
"""
a = frozenset([1,2,3,4])
"""
#globals() #返回当前整个程序里所有的变量 返回形式是K:V 变量名是k 变量是V 仅仅是打印全局变量 不打印局部变量
"""
print(globals())
"""
#hash

#hex
"""
print(hex(2)) #将数字转换成16进制
"""
#locals #将局部变量以K:V的形式打印返回 与globals相反
"""
def test1():
    aaa = 333
    print(locals())
test1()
"""
#max
"""
print(max([1,2,3])) #返回列表里的最大值
"""
#min
"""
print(min([1,2,3])) #返回列表里的最小值
"""
#oct #转换8进制
"""
print(oct(15))
"""
#pow
"""
print(pow(2,2))#返回前一个数字的多少次方
"""
#repr

#round
"""
print(round(1.3333,2)) #保留小数点后的前两位
"""
#sorted 排序 它默认按照字典的key进行排序 从小到大
"""
a = {6:2,8:0,1:4,-5:6,99:11}
print(sorted(a.items()))
"""
"""
a = {6:2,8:0,1:4,-5:6,99:11} #将字典按照Value的值进行排序
print(sorted(a.items(),key= lambda x:x[1]))
"""
#sum #将一个列表的数据求和
"""
print(sum([1,2]))
"""
#zip #拉链拼接 将两个数据整合到一一对应的一起 如果有其中一方数据小于另一方那就按照最少的那个数据进行
"""
a = [1,2,3,4]
b = ['a','b','c','d']
res = zip(a,b)
for i in res:
    print(i)
"""
__import__() #可以直接应用字符串