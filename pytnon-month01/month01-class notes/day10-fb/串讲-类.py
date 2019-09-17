#小明有10000块钱,小白有1000,然后小白问小明借5000,问小白小明各多钱

# class Money:
#     xiaoming_total_money = 10000
#     @classmethod
#     def xiaoming_money(cls):
#         print(cls.xiaoming_total_money)
#     xiaoming = 10000
#     def __init__(self,name,money):
#         self.name = name
#         self.money = money
#         Money.xiaoming_total_money -= money
#
# xiaobai = Money('小白',5000)
#
# Money.xiaoming_money()

class Person:
    def __init__(self,name,money,obj=None):
        self.name = name
        self.money = money
        self.obj = obj
        if self.obj:
            self.borrow()

    def borrow(self):
        # obj.money -= 5000
        self.obj.money -= 5000
        self.money += 5000

xiaoming = Person('小明',10000)
xiaobai = Person('小白',1000,xiaoming)

# xiaobai.borrow(xiaoming)

print('小明有%s,小白有%s.' % (xiaoming.money,xiaobai.money))

