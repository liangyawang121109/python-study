#hashlib模块用于加密相关的操作 3.x里代替了md5和sha模块 主要提供了SHA1 SHA224 SHA256 SHa512 MD5算法
import hashlib
"""
m = hashlib.md5()
m.update(b"hello")
print(m.hexdigest())

m.update(b"it me") 
print(m.hexdigest())

"""
"""
m2 = hashlib.sha256()
m2.update(b"admin")#3.x里加密时必须为b类型的
print(m2.hexdigest())
"""
import hmac

m3 = hmac.new(b'liang',b'yawang')
print(m3.hexdigest())