class dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod #如果类里边的函数加上此静态 那么实际上这个函数就跟这个类就没什么关系了 只不过就是通过这个类调用此函数
    def eat(self,food):#那么调用时这个参数就得全部传入了 它已经不属于类
        print('%s is eating %s'% (self.name,food))


d =dog('honghong')
d.eat('包子')

