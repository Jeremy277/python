'''
继承方法
'''

#代码:功能不是自己写的 但可以直接用

#当多个子类在概念上一致时,考虑抽象出一个父类
#多个子类中的共性提取到父类中
#从设计角度:继承 先有子类 再有父类
#从编码角度:先有父类 再有子类

class Person:
    def say(self):
        print('balabala')

class Student(Person):  #student继承person
    def study(self):
        print('学习')

class Teacher(Person):  #teacher继承person
    def teacher(self):
        print('上课')

stu_1 = Student()
#子类可以直接调用父类成员
stu_1.say()

p01 = Person()
p01.say()
#父类不能直接调用子类成员
# p01.study()  #报错

#Python内置函数
t01 = Teacher()
print(isinstance(t01,Teacher))#True
print(isinstance(t01,Person))#True
print(isinstance(t01,Student))#False

print(issubclass(Teacher,Person))#True
print(issubclass(Teacher,Student))#False
print(issubclass(Person,Teacher))#False