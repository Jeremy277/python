#老张开车去东北 有数据和功能才能定义为类
#老张 车
class Person:
    def __init__(self,name):
        self.name = name
        #面向对象 车自己的数据和行为 组合 将不同类合体 实现一个功能
        self.car = Car(self.name)
    def go_to(self,position,type):
        #1.需要车 耦合性过高
        # Car().run()
        #2.去耦合 定义变量 然后调用类方法
        print(self.name + '去' + position)
        type.run()
        #3.通过组合思想调用类 低耦合
        # print(self.name + '去' + position)
        # self.car.run()

class Car:
    def __init__(self,owner):
        self.owner = owner

    def run(self):
        print('这是%s的车' % self.owner)
        print('开车走')

# c01 = Car()
lz = Person('老张')
ll = Person('老李')
#老张开老李的车
lz.go_to('东北',ll.car)