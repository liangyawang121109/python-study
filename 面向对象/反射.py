

def bulk(self):
    print('%s is eating'% self.name)

class test(object):
    def __init__(self,name):
        self.name = name

    def eat(self):
        print('%s is eating'% self.name)

d = test('liangyawang')
chioce = input('>>>:').strip()
# print(hasattr(d,chioce))
# print(getattr(d,chioce))
# getattr(d,chioce)()
if hasattr(d,chioce):
    #getattr(d,chioce)()
    delattr(d,chioce)
#else:
    #setattr(d,chioce,bulk)
    #d.talk(d)
print(d.name)
#hasattr() 判断一个对象里是否有对应的字符串的方法
#getattr() 根据字符串去获取对象里的对应的方法的内存地址
#setattr() 设置一个值
#delattr() 删除一个属性
