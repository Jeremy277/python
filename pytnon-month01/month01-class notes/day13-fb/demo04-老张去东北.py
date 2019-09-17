#老张开自己的车去东北
#需求有变换:坐飞机 坐火车 骑车

class Vehicle:
    #交通工具 代表所有具体的交通工具
    def transport(self,position):
        #因为父类太过抽象,写不出具体方法体
        pass


class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self,postion,type):
        print('去:'+postion)
        #判断怎么走
        type.transport(postion)

#----------------------------------------------

class Car(Vehicle):
    def transport(self,position):
        print('开车到',position)
class Airplane(Vehicle):
    def transport(self, position):
        print('飞到', position)

#测试代码:
c01 = Car()
a01 = Airplane()
lz = Person('老张')

lz.go_to('东北',c01)
lz.go_to('东北',a01)