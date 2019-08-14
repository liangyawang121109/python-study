#定义两个父类 新式类 让两个子类多继承

class people(object): #定义父类
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s eat dinner'% self.name)

    def sleep(self):
        print('%s are sleeping,his age is %s'% (self.name,self.age))

    def talk(self):
        print('%s are talking'% self.name)

class makefriend(object): #定义第二个新式类
    def jiaoyou(self,obj):
        print('%s is jiao pengyou with %s'% (self.name,obj.name))




class man(people,makefriend):
    pass

m1 = man('liangyawang', 18)
#m1.eat()
#m1.sleep()
#m1.talk()

class woman(people,makefriend):
    def shenghaizi(self):
        print('%s is born a baby'% self.name)

m2 = woman('jingjing',19)
m1.jiaoyou(m2)