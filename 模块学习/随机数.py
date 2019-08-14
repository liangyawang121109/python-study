import random
#print(random.random()) #随机浮点数

#print(random.randint(1,5)) #取1-5范围内的随机整数
#print(random.randrange(3))#取3之前的数字的随机数 不包含3 顾头不顾尾
#print(random.choice([1,2,3])) #可以从列表 字符串中取随机值
#print(random.sample([1,2,3,4,5],2)) #可以从列表 字符串等中随机取两个随机值返回
#print(random.uniform(1,4)) #取1-4之间的浮点数随机值
"""
lis = [1,2,3,4,5,6,7]
random.shuffle(lis) #将列表中的顺序打乱
print(lis)
"""
###随机数生成
cho = ''
for i in range(4):
    if i == random.randrange(0,4):
        tmp = chr(random.randrange(65,69))
    else:
        tmp = random.randint(0,9)
    cho += str(tmp)
print(cho)


