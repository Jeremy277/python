'''
封装
'''


class Wife:
    def __init__(self, name=None, age=None):
        self.name = name
        # 私有成员:以双下划线开头
        self.__age = age
        # self.set_age(age)

    def __str__(self):
# 为对象创建字符串表示方式:当对象被打印时显示此字符串
        # obj = '你好!'
        # obj += self.name
        # return obj
        return self.name
    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 25:
            self.__age = value
        else:
            # 抛出异常
            raise ValueError('超过25岁')


w01 = Wife('李知恩', 25)
# 不能访问私有变量
# print(w01.name,w01.__age)
# w01.set_age(25)
print(w01.get_age())
#python通过一种特殊的命名规则来隐藏特性的,
# 用_类__变量,可直接从类定义的外部访问私有特性,私有方法访问方法类似
# print(w01._Wife__age)
# 为对象创建字符串表示方式:def __str__(self):
# 当对象被打印时显示此字符串
print(w01)
