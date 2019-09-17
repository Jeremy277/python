#定义老婆类 创建3个老婆对象
class Wife:
    wife_count = 0
    @classmethod
    def print_wife_count(cls):
        print('wife的数量:',cls.wife_count)

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Wife.wife_count +=1

list_1 = [
    Wife('貂蝉',18),
    Wife('西施',17),
    Wife('昭君',19)
]
# for item in list_1:
#     print('我的老婆是:',item.name)
print('老婆数量:',Wife.wife_count)

Wife.print_wife_count()
