# a = 1 and 2
# print(a)
#
# a = 8 and 2 and 6
# print(a)
#
# list_ = [[]] * 5
# print(list_)
# list_[0].append(1)
# print(list_)
# list_[1].append(2)
# print(list_)
# list_.extend([3])
# print(list_)
# list_.append([3])
# print(list_)
# list_.append(3)
# print(list_)

class Person:
    def __init__(self):
        self.a = [1]
        self.b = {2}
        self.c = (3,)

    def test(self):
        self.d = 4
        print('hahah')

    def test1(self):
        print('d:',self.d)



zu = Person()
zu.test()  #hahah
print(zu.a)
print(zu.b)
print(zu.c)
print(zu.d) # 4
# zu.test()  #hahah
zu.test1()  #d: 4


