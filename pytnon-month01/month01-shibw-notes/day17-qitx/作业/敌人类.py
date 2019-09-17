# 3. 创建敌人类(姓名,血量,攻击力,防御力)
#    创建敌人列表，存储若干敌人.
#    -- (1) 在敌人列表中查找所有死人
#    -- (2) 在敌人列表中查找血量最大的敌人
#    -- (3) 在敌人列表中查找所有敌人姓名与攻击力
class Enemy:
    def __init__(self,name,hp,atk,defence):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence
    def __str__(self):
        return self.name


list_enemy = [
    Enemy('灭霸', 100, 99, 89),
    Enemy('亡刃将军', 90, 80, 70),
    Enemy('暗夜比邻星', 90, 79, 69),
    Enemy('乌木喉', 0, 69, 59),
    Enemy('黑矮星', 70, 59, 39),
    Enemy('超巨星', 60, 49, 79),
    Enemy('黑暗犬', 0, 19, 19, )
]
#    -- (1) 在敌人列表中查找所有死人
def find_dead():
    for item in list_enemy:
        if item.hp == 0:
            yield item
for item in find_dead():
    print(item)
# for item in (item for item in list_enemy if item.hp == 0):
#     print(item)
#将惰性操作 --> 改为立即操作 以 取出第一个元素
result = tuple(find_dead())
print(result)
#    -- (2) 在敌人列表中查找血量最大的敌人
def find_maxhp():
    max_hp = list_enemy[0]
    for i in range(1,len(list_enemy)):
        if list_enemy[i].hp > max_hp.hp:
            max_hp = list_enemy[i]
        return max_hp
print(find_maxhp())
#    -- (3) 在敌人列表中查找所有敌人姓名与攻击力
def print_info():
    for item in list_enemy:
        yield (item.name,item.atk)
re = print_info()
for item in re:
    print(item)
#只能调用一次
for item in re:
    print(item)
# for item in ((item.name,item.atk) for item in list_enemy ):
#     print(item[0],item[1])




