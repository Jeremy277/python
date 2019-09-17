#为孩子买一个玩具LittlePony
# class LittlePony:
#     def __init__(self,litter,middle,large):
#         self.litter = litter
#         self.middle = middle
#         self.large = large
#
#     @property
#     def litter(self):
#         return self.__litter
#     @litter.setter
#     def litter(self,value):
#         if 0 <= value <= 100:
#             self.__litter = value
#         else:
#             raise ValueError('litter不在范围')
#
#     @property
#     def middle(self):
#         return self.__middle
#     @middle.setter
#     def middle(self, value):
#         if 0 <= value <= 100:
#             self.__middle = value
#         else:
#             raise ValueError('middle不在范围')
#
#     @property
#     def large(self):
#         return self.__large
#     @large.setter
#     def large(self, value):
#         if 0 <= value <= 100:
#             self.__large = value
#         else:
#             raise ValueError('large不在范围')

#玩具类
class LittlePony:
    def __init__(self,size,color):
        self.size = size
        self.color = color
        #面向对象 组合 将不同类合体 实现一个功能
        self.vendor = Vendor()

    def sing(self):
        print('lalala')

    def speak(self):
        print('hello my name is LittlePony')

#玩具的厂家属性类
class Vendor:
    def __init__(self,email='LittlePony@emial.cn',
                 phone='400-123-8989',
                 address='地球1区'):
        self.email = email
        self.phone = phone
        self.address = address

    def call(self):
        print('给%s打电话' % self.phone)

myLittlePony = LittlePony('middle','pink')
myLittlePony.vendor.call()
print(myLittlePony.vendor.address)


