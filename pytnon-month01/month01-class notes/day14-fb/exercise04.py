#实现字符串减法

class Str01(str):
    pass

    def __sub__(self, other):
        return self.replace(other,'')


s01 = Str01(1234)
s02 = Str01(23)
print(s01-s02)
