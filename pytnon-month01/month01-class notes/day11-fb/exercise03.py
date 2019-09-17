'''
面向对象
'''
#创建技能skill
class Skill:
    def __init__(self,name,atk_ration,duration,mp_cons):
        self.name = name
        self.atk_ration = atk_ration
        self.duration = duration
        self.mp_cons = mp_cons

    @property
    def atk_ration(self):
        return self.__atk_ratio
    @atk_ration.setter
    def atk_ration(self,value):
        if 0.1 <= value <= 5:
            self.__atk_ratio = value
        else:
            raise ValueError('攻击比例不在范围')

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, value):
        if 0.1 <= value <= 10:
            self.__duration = value
        else:
            raise ValueError('持续时间不在范围')

    @property
    def mp_cons(self):
        return self.__mp_cons
    @mp_cons.setter
    def mp_cons(self, value):
        if 0 <= value <= 100:
            self.__mp_cons = value
        else:
            raise ValueError('消耗法力不在范围')


skill_1 = [
    Skill('降龙十八掌',5,9,80),
    Skill('九阴白骨爪',4,7,50),
    Skill('一阳指',5,2,60),
    Skill('打狗棒法',2,10,0)
]

#1.查找降龙十八掌
def find():
    for item in skill_1:
        if item.name == '降龙十八掌':
            return item
# item = find()
# if item:   #先判断
#     print('查找降龙十八掌:',item.name)

#2.查找不消耗法力的技能
def find_mp():
    result = []
    for item in skill_1:
        if item.mp_cons == 0:
            result.append(item)
    return result
# res = find_mp()
# for item in res:
#     print('不消耗法力的技能:',item.name)
#3.查找所有技能以及持续时间
# def find_all():
#     # list_1 = []
#     for item in skill_1:
#         print(item.name, item.duration)
# print('查找所有技能以及持续时间:')
# find_all()
def find_3():
    # result = {}
    # for item in skill_1:
    #     result.setdefault(item.name,item.duration)
    return {item.name:item.duration for item in skill_1}

# res = find_3()
# for k,v in res.items():
#     print(k,v)
#4.删除所有不消耗法力的技能:
def del_mp():
    count = 0
    list_1 = []
    for i in range(len(skill_1)-1,-1,-1):
        if skill_1[i].mp_cons == 0:
            # print(skill_1[i].name)
            list_1.append(skill_1[i].name)
            del skill_1[i]
            count += 1
    return list_1,count
# print('删除所有不消耗法力的技能:')
#
# print(del_mp())

#5.查找攻击比例最大的技能
# def find_atk():
#     max_1 = skill_1[0].atk_ration
#     for i in range(1,len(skill_1)):
#         if max_1 < skill_1[i].atk_ration:
#             max_1 = skill_1[i].atk_ration
#     return max_1
# print('\n查找攻击比例最大的技能:')
# max_1 = find_atk()
# for item in skill_1:
#     if item.atk_ration == max_1:
#         print(item.name)
# print('\n查找攻击比例最大的技能:')
# max_1 = find_atk()
# for item in skill_1:
#     if item.atk_ration == max_1:
#         print(item.name)
def find_atk():
    max_1 = skill_1[0]  #赋值要灵活
    for i in range(1,len(skill_1)):
        if max_1.atk_ration < skill_1[i].atk_ration:
            max_1 = skill_1[i]
    return max_1
# print('\n查找攻击比例最大的技能:')
# res = find_atk()
# print(res.name,res.atk_ration)

#6.对技能列表按照持续时间升序排列
def sort_dur():
    for r in range(len(skill_1)-1):
        for c in range(r+1,len(skill_1)):
            if skill_1[r].duration > skill_1[c].duration:
                skill_1[r],skill_1[c] = skill_1[c],skill_1[r]


sort_dur()
print('技能列表按照持续时间升序排列:')
for item in skill_1:
    print(item.name,item.duration)











