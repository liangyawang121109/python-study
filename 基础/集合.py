list1 = [1,2,3,5,4,6]
list2 = [8,4,2,6,1,9]
list1= set(list1)

#print(list1,type(list1))
#求交集
#print(list1.intersection(list2))
#print(list1 & list2) 求交集的第二种方法
#求并集
#print(list1.union(list2))
#print(list1 | list2) 求并集的第二种方法
#求差集 取出list1里边有的 list2里边没有的
#print(list1.difference(list2))
#print(list1 - list2) 求差集的第二种方法
#求子集
#print(list1.issubset(list2))
#求父集
#print(list1.issuperset(list2))
#对称差集 将两边的交集去掉 将两个列表里互相都没有的取出来放在一起
#print(list1.symmetric_difference(list2))
#print(list1 ^ list2) 求对称差集的第二种方法
#检测两个列表是否有交集 如果没有返回true 如果有返回false
list3 = set([1,2,3])
list4 = set([1,2,3])
#print(list3.isdisjoint(list4))
#对集合添加数据
#list3.add(999)
#print(list3)
#对集合添加多个数据
#list3.update([33,22])
#print(list3)
#删除集合中的一个项
#list3.remove(1) #如果这个值不存在他会报错
#list3.discard(1) #如果这个值不存在返回none
#print(list3)
#计算集合的长度
#print(len(list3))
#判断是否在这个集合里
#print(5 in list3)
