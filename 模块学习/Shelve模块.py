import shelve

#shelve是一个简单的k v将内存数据通过文件持久化的模块 可以持久化任何pickle可支持的python数据
"""
#写入
d = shelve.open('sh_test')
name = ['liangyawang','liangjing']
info = {
    'age':22,
    'sex':'man'
}

d["info"] = info
d['name'] = name
d.close()
"""

#读取
d = shelve.open('sh_test')
print(d.get('info'))
print(d.get('name'))
