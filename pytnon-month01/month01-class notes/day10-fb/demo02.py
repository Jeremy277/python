class Wife:
    pass

w01 = Wife()
w01.name = '赵敏'
print(w01.name)

# w02 = Wife()
# print(w02.name)#AttributeError: 'Wife' object has no attribute 'name'
#可以通过


print(w01.__dict__)#{'name': '赵敏'}
# print(w02.__dict__)

class Wife2:
    #构造函数,添加实例变量
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #实例方法
    def print_self(self):
        print(self.name,self.age)

w01 = Wife2('zhaomin',28)
w01.print_self()
Wife2.print_self(w01)#不建议使用