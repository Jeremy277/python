#创建model02.py
#定义函数my_fun()
#d第一Myclass02
#包含 #构造函数 实例方法 类方法
def my_fun():
    print('my_fun函数')

class Myclass02:
    def __init__(self,a):
        self.a = a
    def fun02(self):
        print('fun02实例方法')

    @classmethod
    def fun03(cls):
        print('fun03类方法')
