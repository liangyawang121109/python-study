class dog(object):
    def __init__(self,name):
        self.name = name
        self.__food = None

    @property #属性方法 将一个方法变成一个静态属性  当把它转换成一个属性后 默认是不可以在调用的时候给属性赋值的需要在写一个特殊处理 如下
    def eat(self):
        print('%s is eating %s'% (self.name,self.__food))

    @eat.setter
    def eat(self,food):
        print('%s is eating %s'% (self.name,food))
        self.__food = food
    @eat.deleter
    def eat(self):
        del self.__food
d = dog('user')
d.eat
d.eat = 'baozi'
#del d.name 删除普通属性
#将方法转换成静态属性后 默认是不能删除的 需要做进一步处理
del d.eat
d.eat