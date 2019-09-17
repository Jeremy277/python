"""
    练习1:
        需求:在技能列表中,查找编号是102的技能对象.
            在技能列表中,查找名称是九阳神功的技能对象.
        封装:将变化点与通用代码定义到函数中.
        继承:在通用代码中抽象变化点
        将通用代码写到ListHelper中
        在当前模块中调用.

"""
from common.list_helper import ListHelper


class Skill:
    def __init__(self, id, name=None, atk=None, duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

    def __str__(self):
        return self.name

list01 = [
    Skill(101,"乾坤大挪移",8000,30),
    Skill(102,"九阳神功",9000,50),
    Skill(103,"九阴白骨爪",500,10),
    Skill(104,"黑虎掏心",9800,40),
    Skill(105,"葵花宝典",6000,2),
]
#函数体  查找多个元素
def condition01(item):
    return item.duration > 10

def condition02(item):
    return 102 <= item.id <=105
#函数体  查找单个元素
def condition03(item):
    return item.id == 102

def condition04(item):
    return item.name == '九阳神功'

#调用函数查找多个元素
for item in ListHelper.find_all(list01,condition01):
    print(item)
#调用函数查找单个元素
re = ListHelper.find_single(list01,condition03)
print(re.name)
#将调用函数方法改为lambda
for item in ListHelper.find_all(list01,lambda item:item.duration >10):
    print(item)

re = ListHelper.find_single(list01,lambda item:item.id == 102)
print(re.name)
#-------------------------------
#1.计算所有攻击力之和
# def sum_atk():
#     sum_atk = 0
#     for i in range(len(list01)):
#         sum_atk += list01[i].atk
#     return sum_atk
# print(sum_atk())
# def sum_atk():
#     sum_atk = 0
#     for item in list01:
#         sum_atk += item.atk
#     return sum_atk
# print(sum_atk())



re = ListHelper.sum_data(list01,lambda item:item.atk)
print(re)
#2.获取技能名称和持续时间
# def get_data():
#     for item in list01:
#         yield (item.name,item.duration)
# for item in get_data():
#     print(item)

for item in ListHelper.get_data(list01,lambda item :(item.name,item.duration)):
    print(item)
#3.获取攻击力最大的技能
re = ListHelper.max_data(list01,lambda item:item.atk)
print(re)
#4.对攻击力进行升序排列
# for item in ListHelper.sort_data(list01,lambda item:item.atk):
#     print(item.name)
# print('')
ListHelper.sort_data(list01,lambda item:item.duration)
for item in list01:
    print(item)

#1.获取长度最长的元素
list02 = ([1,1],[2,2,2,2],[3,3])
print(max(list02,key = lambda i:len(i)))
#2.获取技能列表所有名称 持续时间 攻击力
for item in map(lambda  item:item,list01):
    print(item.name,item.duration,item.atk)
#3.获取攻击力最小
print(min(list01,key=lambda item:item.atk))
#4.持续时间降序排列
for item in sorted(list01,key=lambda item:item.duration,reverse=True):
    print(item.duration)