#张无忌 教 赵敏 乾坤大挪移
#赵敏 教 张无忌 化妆
#张无忌 上班 挣了 10000
#赵敏 上班 挣了 6000

#人类
class Person:
    def __init__(self,name):
        self.name = name

    def teach(self,person,skill):
        print(self.name,'教',person.name,skill)

    def work(self,money):
        print(self.name,'上班挣了',money)

zhangwuji = Person('张无忌')
zhaomin = Person('赵敏')

zhangwuji.teach(zhaomin,'乾坤大挪移')
zhaomin.teach(zhangwuji,'化妆')

zhangwuji.work(10000)
zhaomin.work(6000)


