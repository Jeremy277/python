#运算符重载
class Vector1:
    def __init__(self, x):
        self.x=x
    def __str__(self):
        return '%s' % self.x
#算数运算符重载
    def __add__(self, other):
        return Vector1(self.x+other)
    def __sub__(self, other):
        return Vector1(self.x-other)
    def __mul__(self, other):
        return Vector1(self.x*other)
    def __truediv__(self, other):
        return Vector1(self.x / other)
    def __floordiv__(self, other):
        return Vector1(self.x // other)
    def __mod__(self, other):
        return Vector1(self.x % other)
#反向算数运算符重载
    def __radd__(self, other):
        return Vector1(self.x + other)
#复合运算符重载
    def __iadd__(self, other):
        self.x += other
        return self
#比较运算重载
    def __lt__(self, other):
        if self.x > other:
            return True
        return False


v01 = Vector1(10)
print(v01,id(v01))#10 140515542780672
# print(v01+2)#正向
# print(2+v01)#反向
v01 += 2#产生新对象 因此#需要复合运算符重载
print(v01,id(v01))#12 140515542780672
# v02 = Vector1(14)
# print(v02-3)
# print(v02*3)
# print(v02/3)
# print(v02//3)
# print(v02%3)
# print(v02**3)#报错没有重载**运算符

print(v01<12)