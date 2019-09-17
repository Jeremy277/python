# 老张去东北  day11-fanb/demo06.py
# 需求变化 ： 坐飞机
#           坐火车
#           骑车

# Dependency Inversion Principle
# 客户端代码(调用的类)尽量依赖(使用)抽象。
# 抽象不应该依赖细节，细节应该依赖抽象
class Vehicle:
    #交通工具  代表所有的具体的交通工具
    #
    def transport(self,position):
        #因为父类太抽象，写不出具体的方法体
        pass

class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self,position,vehicle):
        print('去：' + position)
        vehicle.transport(position)

#上边抽象代码不需要修改,改动只改变下边的具体代码
# ----------------------------------------

class Car(Vehicle):

    def transport(self, position):
        print('开车到', position)

# def transport(self,position):
    #     print('开车到',position)


class Airplane(Vehicle):
    def transport(self,position):
        print('飞到',position)

c01 = Car()
a01 = Airplane()
lz = Person('老张')
lz.go_to('东北', c01)
lz.go_to('东北', a01)