#class people :经典类
#class peopel(object):新式类

class people: #定义父类
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s eat dinner'% self.name)

    def sleep(self):
        print('%s are sleeping,his age is %s'% (self.name,self.age))

    def talk(self):
        print('%s are talking'% self.name)

"""
class man(people): #定义子类 继承父类的属性方法
    pass

m1 =man('liangyawang',18) #然后给子类传值
m1.eat() #调用子类 然后调用父类的方法
m1.sleep()
m1.talk()
"""

#也可以在继承父类的方法的同时在子类里边定义一些子类自己的方法
"""
class man(people):
    def tiao(self):
        print('%s are tiao'%self.name)

m1 = man('liangyawang',18)
m1.tiao()
"""
#子类在继承父类的时候重构父类的方法
"""
class man(people):
    def eat(self):
        people.eat(self) #将父类的方法拿过来 然后重构方法
        print('%s is chichichi '%self.name)


m1 = man('liangyawang',18)
m1.eat()
"""
#子类不可调用兄弟子类的方法
"""
class woman(people):
    def shenghaizi(self):
        print('%s is born a baby'% self.name)


m1 = woman('jingjing',18)
m1.shenghaizi()
"""

#单子类在继承父类的同时 还需要增加功能 但是父类不能增加 否则影响其它子类 如下：
"""
class man(people):
    def __init__(self,name,age,money):
        people.__init__(self,name,age) #另一种写法 super(man.self).__init__(name,age)
        self.money = money
    def info(self):
        print('%s age: %s have money:%s'%(self.name,self.age,self.money))

m1 = man('liangyawang',18,15000)
m1.info()
"""
