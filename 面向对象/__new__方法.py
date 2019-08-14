'''
class foo(object):
    def __init__(self,name):
        self.name =name

f = foo('liangyawang')
print(type(f))
print(type(foo))
'''

'''
def func(self):
    print('hello liangyawang %s age %s'% (self.name,self.age))
def __init__(self,name,age):
    self.name = name
    self.age = age
foo = type('foo',(object,),{'talk':func,
                            '__init__':__init__})
f = foo('liangyawang',18)
f.talk()

print(type(foo))

'''

class foo(object):
    def __init__(self,name):
        self.name = name
        print('foo init__')
    def __new__(cls, *args, **kwargs): #new是用来创建实例的
        print('foo new__')
#        return object.__new__(cls)

f = foo('liangyawang')

