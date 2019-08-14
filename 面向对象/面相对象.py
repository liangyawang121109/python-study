class role:
    n = 3 #类变量 存储在类的内存中
    def __init__(self,name,role,life_value=100,money=15000):
        #构造函数
        self.name = name #实例变量又叫做静态属性 作用域实例本身
        self.role = role
        self.__life_value = life_value #定义一个私有属性 私有属性在外部是不能够被访问的 定义一个方法进行访问
        self.money = money

    def show_status(self): #私有属性在内部可以更改 访问 所以定义的私有属性需要在内部定义方法进行访问
        print('name:%s role:%s life_value:%s'%(self.name,
                                                   self.role,
                                                   self.__life_value))


    def shot(self): #类的方法 也就是这个类的功能 也算是一个动态属性
        print("shooting")

    def __got_shot(self): #定义一个私有方法 同样不能再外边访问 更改
        print("%s:i,got shot "% self.name)

    def buy_gun(self,gunname):
        print("%s just bought %s"% (self.name,gunname))

    def __del__(self): #x析构函数 在实例 释放或销毁的时候自动执行 通常用于一些收尾工作 如 关闭数据库链接 关闭打开的临时文件
        pass


r1 = role('liangyawang','police')
r1.buy_gun('B22')
r1.n = 5 #类变量可被实例在每个实例的范围内进行修改 再下一个实例中不被改变
print(r1.n)
print(r1.show_status())
#del r1 #删除实例

#面向对象三大特性 封装 继承 多态


