#在python3里全是 广度优先继承查询策略
"""
class A:
    def __init__(self):
        print("in class A")

class B(A):
    def __init__(self):
        print("in class B")

class C(A):
    def __init__(self):
        print('in class C')

class D(B,C):
    pass

obj = D()
"""
#在python2里经典类是深度优先 而如果加上object新式类 那么就是按照广度优先继承
