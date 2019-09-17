#定义DOG类

class Dog:
    def __init__(self,name,kinds,color):
        self.name = name
        self.kinds = kinds
        self.color = color
    def eat(self,food):
        print('%s的%s正在吃%s' %
              (self.color,self.name,food))
    def run(self,speed):
        print('%s%s正以时速%s飞奔' %
              (self.kinds,self.name,speed))
#创建Dog对象
# 调用__init__构造函数
bingtang = Dog('冰糖','博美','雪白')
xueli = Dog('雪梨','二哈','银白')

bingtang.eat('牛肉')
xueli.run('45km/h')
#将Dog对象地址赋值给doudou(两个变量指向一个对象)
doudou = bingtang
# doudou.eat('狗粮')
# bingtang.eat('排骨')

doudou.name = '豆豆'
bingtang.eat('火腿肠')

list_1 = [bingtang,doudou,Dog
('儿子','哈士奇','灰色')]
list_2 = list_1
list_1[2].color = '白色'
print(list_2[2].color)#白色