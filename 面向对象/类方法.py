class dog(object):
    name = 'honghong'
    def __init__(self,name):
       self.name = name

    @classmethod #类方法 只能访问类变量 不能访问实例变量
    def eat(self,food):
        print('%s is eating %s'% (self.name,food))


d =dog('yayayaya')
d.eat('包子')