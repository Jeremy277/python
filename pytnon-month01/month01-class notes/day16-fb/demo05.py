#raise
from demo06 import AgeError
class Wife:
    def __init__(self, age):
        self.age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 18 <= value <= 24:
            self.__age = value
        else:
            # raise ValueError('年龄不合适')
            raise AgeError('年龄不合适',
            '18 <= value <= 24',101)

try:
    w01 = Wife(100)
    print(w01.age)
# except ValueError as e:
#     print(e.args)  #信息('年龄不合适',)
except AgeError as e:
    print(e.id)  #信息('年龄不合适',)
    print(e.message,e.code)  # 信息('年龄不合适',)
    print(e.args)#('年龄不合适', '18 <= value <= 24', 101)