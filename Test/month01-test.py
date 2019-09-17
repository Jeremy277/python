# d = {"a": 3, "b": 2, "c": 1}
# print('b' in d)
# # x = [1, 'Two', 3, 'Four']
# # y = [1, 'Two', 3, 'Four']
# # z = [1]
# # print(x[2:3] == 3)
# # print(x is y)
# # print(x == y)
# # x,y = (20, 30)
# # print(x)
# # print(y)
# class A:
#    a = 1
# obj = A()
# obj.a = 2
# print(obj.a)
# print(A.a)
# A.a = 3
# print(obj.a)
#
# for x in range(5, 0, -2):
#           print(x)
#
# print("/".join(["C:", "Programe Files", "Python3"]))
#
#
# a = 21 % 2.5
# print(a)

# def fun01():
#     yield 1
#
# fun01()

L = [1,2,3]
def func(a):
     a = [4,5,6]
func(L)
print(L)

class A():
    v = 100
    def __init__(self):
        self.v = 200
class B(A):
    v = 300
    def __init__(self):
        self.v = 400
        super().__init__()
a = B()
print(a.v)

L1 = [1, 2, 3]
L2 = [L1, 4, 5]
L3 = L2
L4 = L3.copy()
L1[1] = 10
L3[1] = 40
L4[2] = 50

print(L1)
print(L2)
print(L3)
print(L4)

# a = {1,2,3,4,5,6}和b = {5, 6, 7, 8, 9}，
# c = {5, 6}，d = {5, 6, 7}
class A:
    v = 100
    def __init__(self):
        self.v = 200
a1 = A()
a2 = A()
del a2.v

print(A.v)
print(a1.__class__.v)
print(a2.v)
print(a1.v)
L = [1,2,3]
def func(a):
     a = [4,5,6]
func(L)
print(L)









x = {"0", 1, 3, 4, 8}
# print(sum(x))
# max(x)
print(any(x))
print(len(x))



a = {1,2,3,4,5,6}
b = {5, 6, 7, 8, 9}
c = {5, 6}
d = {5, 6, 7}
print(d < d - c | a)
num = 1
while num <= 20:
    print(num)
    num += 1
else:
    print("打印完毕")

print ("%s 今年 %d 岁"  %  ("小明", 20))