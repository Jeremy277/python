# 2.小明去银行取钱
# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     def go_to(self,dowhat,where):
#         print(dowhat)
#         where.here()
#
# class Where:
#     def here(self):
#         print('银行')
#
# w01 = Where()
# xiaoming = Person('小明')
# xiaoming.go_to('取钱',w01)

class Person:
    def __init__(self, name, money=None):
        self.name = name
        self.money = money

class Bank:
    def __init__(self,money):
        self.money = money

    def draw_money(self,target,value):
        if value <= 0:
            # print('value不能小于0')
            #程序报错停止
            raise ValueError('value不能小于0')
            #return 不影响用户继续使用程序
            # return 'value不能小于0'
        print(target.name,'在取',value,'钱')
        self.money -= value
        target.money += value
        print('%s现在有%s元' % (target.name,target.money))


xiaoming = Person('小明',0)
zs = Bank(1000000)
zs.draw_money(xiaoming,1000)
print(zs.draw_money(xiaoming,-1000))
zs.draw_money(xiaoming,1000)







