'''
    高阶函数
'''
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

#查找死人：
#获取长度最长的元素
list01 = ([1,1],[2,2,2,2],[3,3])
print(max(list01,key = lambda i:len(i)))