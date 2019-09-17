class Person:
    def __init__(self, name = 'jer',score = 99):
        self.name = name
        self.score = score

    def say(self):
        print('说话')

class Student(Person):
    #子类若没有构造函数 使用父类的
    pass

class Teacher(Person):
    #若子类有构造函数 会覆盖父类的构造函数
    #要想使用父类的构造函数中的属性
    #必须先调用父类构造函数
    def __init__(self, age):
        super().__init__()  #若父类需要传参此处必须传参
        self.age = age

s01 = Student()
s01.say()  #说话
print(s01.name) #jer
print(s01.score) #99

t01 = Teacher(28)
t01.say() #说话
print(t01.age) #28
print(t01.name) #jer
print(t01.score) #99

