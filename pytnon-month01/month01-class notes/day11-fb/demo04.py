'''
只读age
'''
class Wife:
    def __init__(self, name=None):
        self.name = name
        self.__age = 25

    @property
    def age(self):
        return self.__age
    # @age.setter
    # def age(self, value):
    #     if 20 <= value <= 25:
    #         self.__age = value
    #     else:
    #         print('超范围')
w01 = Wife('李知恩')
# w01.age = 2
# print(w01.age)

#只写 age
'''
封装
'''
class Wife:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def set_age(self, value):
        if 20 <= value <= 25:
            self.__age = value
        else:
            print('超范围')
    age = property(None,set_age)

w01 = Wife('李知恩',26)

# w01.age = 25
print(w01.name)
