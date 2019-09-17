'''
封装
'''
class Wife:
    def __init__(self, name=None, age=None):
        self.name = name
        #私有成员:以双下划线开头
        # self.__age = age
        # self.set_age(age)
        self.age = age

    @property  #拦截读取 age = property(get_age, None)
    def age(self):
        return self.__age
    #设置写入方法age.setter(写入方法)
    @age.setter#拦截写入
    def age(self, value):
        if 20 <= value <= 25:
            self.__age = value
        else:
            #抛出异常
            # raise ValueError('超过范围')
            print('超范围')
    #拦截对age的读写操作
    # age = property(get_age, set_age)

w01 = Wife('李知恩',25)
#不能访问私有变量
# print(w01.name,w01.__age)
# w01.set_age(25)
# print(w01.get_age())
# w01.age = 25
print(w01.age)
print(w01)

