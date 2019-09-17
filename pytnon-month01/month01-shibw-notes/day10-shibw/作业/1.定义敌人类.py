# 定义敌人类
# 数据 姓名 血量 法力 基础攻击 防御力
# 行为 打印数据信息
#
# 创建敌人列表（至少4个元素）画出内存图
# 查找叫“灭霸”的敌人  打印信息
# 查找所有死亡的敌人
# 计算所有敌人的平均攻击力
# 删除防御力小于10的敌人
# 将所有敌人攻击力增加50

class Enemy:
    def __init__(self, name, hp, mp, attack, defence):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.attack = attack
        self.defence = defence
    def print_info(self):
        print('姓名:%s,血量:%s,法力:%s,攻击力:%s,防御力:%s' %
              (self.name,self.hp,self.mp,self.attack,self.defence))

list_1 = [
    Enemy('灭霸',10000,9999,8999,7999),
    Enemy('亡刃将军',9000,8999,7999,6999),
    Enemy('暗夜比邻星',9000,7999,6999,5999),
    Enemy('乌木喉',8000,6999,5999,4999),
    Enemy('黑矮星',7000,5999,3999,7999),
    Enemy('超巨星',6000,4999,7999,6999),
    Enemy('黑暗犬',0,99,79,69)
]
# 查找叫“灭霸”的敌人  打印信息
def find():
    for item in list_1:
        if item.name == '灭霸':
            return item

info_1 = find()
if info_1:
#     # print(info_1.name)
    info_1.print_info()
else:
    print('该敌人不存在')

# 查找所有死亡的敌人
def find_death():
    for item in list_1:
        if item.hp == 0:
            print('死亡的敌人:',item.name)
find_death()
# 计算所有敌人的平均攻击力
def ave_attack():
    all_attack = 0
    for item in list_1:
        all_attack += item.attack
    return all_attack/len(list_1)

print('敌人平均攻击力:',ave_attack())

# 删除防御力小于6000的敌人
def del_defence():
    for i in range(len(list_1)-1,-1,-1):
        if list_1[i].defence <7000:
            del list_1[i]

del_defence()
for item in list_1:
    print('防御力高于7000的敌人:',item.name)

# 将所有敌人攻击力增加500
for item in list_1:
    item.attack += 500
print('所有敌人攻击力增加500:')
for item in list_1:
    print('敌人:%s 增加后攻击力:%s ' % (item.name,item.attack))



