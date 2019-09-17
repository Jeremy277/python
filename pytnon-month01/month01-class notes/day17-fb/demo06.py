"""
    函数式编程 应用 -- 将函数作为参数
"""

list01 = [4,5,5,65,5,6]
def fun01():
    for item in list01:
        if item % 2:
            yield item

def fun02():
    for item in list01:
        if item > 10:
            yield item

def fun03():
    for item in list01:
        if 3 <item < 10:
            yield item

# 面向函数：
#   "封装"：分
def condition01(item):
    return item % 2 == 1

def condition02(item):
    return item > 10

def condition03(item):
    return 3 <item < 10


#   "继承"：隔(通过参数，抽象具体函数。)
# “万能查找”
def fun(func_condition):
    for item in list01:
        # if 3 <item < 10:
        # if condition03(item):
        #   "多态"：做
        if func_condition(item):
            yield item

fun(condition01)

# 练习:
# 在技能列表中，获取持续时间大于10的所有技能
# 在技能列表中，获取编号在102 -- 105之间的所有技能
# 步骤1：实现功能
# 步骤2：封装--提取变化与不变的代码
# 步骤3：定义"万能查找"方法
# 步骤4：将不变与变化的方法相互结合
class Skill:
    def __init__(self, id, name=None, atk=None, duration=None):
        self.id = id
        self.name = name
        self.atk = atk
        self.duration = duration

    # 对象 --》 字符串
    def __str__(self):
        return self.name

list_1= [
    Skill(101,"乾坤大挪移",8000,30),
    Skill(102,"九阳神功",9000,50),
    Skill(103,"九阴白骨爪",500,10),
    Skill(104,"黑虎掏心",9800,40),
    Skill(105,"葵花宝典",6000,2),
]

def fun_(func_condition):
    for item in list_1:
        if func_condition(item):
            yield item

def condition05(item):
    return item.duration >10
def condition06(item):
    return 102 <=item.id<= 105

fun_(condition05)
for item in fun_(condition05):
    print(item,end=' ')
print('')
for item in fun_(condition06):
    print(item,end=' ')
print('')
# 生成器表达式
for item in (item for item in list_1 if condition05(item)):
    print(item,end=' ')

