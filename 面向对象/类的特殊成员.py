class test(object):
    '''打印狗叫'''
    def __init__(self,name):
        self.name = name

    def dog(self):
        print('%s is wanf wanf wanf'% self.name)
    def __call__(self, *args, **kwargs):
        print('running call',args,kwargs)
    def __str__(self): #当类里边定义了str 那么在打印对象时 默认输出该方法的返回值
        return "name:%s"% self.name
do = test('tiaotiao')

'''
print(do) 打印类里边定义str方法时返回的值
'''

'''
do(1,2,3,name='test')
'''

'''
do.dog()
print(test.__doc__) #打印出类里边的注释的信息
print(do.__module__) #当这个类文件是从别的模块目录里调用的时候可使用此方法查看这个类属于哪个模块
print(do.__class__) #输出这个类的本身 也就是既可以看到它属于哪个模块也可以看到他的类名称
'''

'''
print(test.__dict__) #以字典的形式 将类里边所有的属性打印 不包括实例属性 通过类调用
print(do.__dict__) #以字典的形式 将实例化的所有属性方法打印 不包括类属性 通过实例调用
'''
