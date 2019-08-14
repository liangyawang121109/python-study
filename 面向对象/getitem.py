class foo(object):
    def __getitem__(self, key):
        print('__getitem__',key)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)

    def __delitem__(self, key):
        print('__delitem__',key) 9

obj = foo()
obj['name'] = 'liangyawang' #自动触发执行setitem 以字典的形式赋值
print(obj['name']) #自动触发执行getitem 获取
del obj['name'] #自动触发 delitem 删除

