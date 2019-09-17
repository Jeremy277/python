'''
封装
'''
class Wife:
    def __init__(self, name=None, age=None):
        self.name = name
        #私有成员:以双下划线开头
        self.__age = age
        # self.set_age(age)
        # self.age = age
    def __str__(self):
#为对象创建字符串表示方式:当对象被打印时显示此字符串
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
            #抛出异常
            raise ValueError('超过范围')
    #拦截对age的读写操作
    age = property(get_age, set_age)

w01 = Wife('李知恩',26)
#不能访问私有变量
# print(w01.name,w01.__age)
# w01.set_age(25)
# print(w01.get_age())
print(w01.age)
# print(w01)
