#特性 一种接口多种实现

def anymal(obj):
    obj.talk()

class cat:
    def talk(self):
        print('miao')

class dog:
    def talk(self):
        print("wang")
c = cat()
d = dog()
anymal(c)
anymal(d)
