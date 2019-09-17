# 玩家(攻击力)攻击敌人(血量)敌人受伤(减血)可能死亡(播放动画)
# 敌人攻击玩家 玩家受伤(减血 碎屏) 可能死亡(游戏结束)

# class Player:
#     def __init__(self,name,hp,atk):
#         self.name = name
#         self.hp = hp
#         self.atk = atk
#
#     @property
#     def hp(self):
#         return self.__hp
#     @hp.setter
#     def hp(self,value):
#         if 0<=value<=100:
#             self.__hp = value
#         else:
#             raise ValueError('血量不在区间内')
#
#     @property
#     def atk(self):
#         return self.__atk
#
#     @atk.setter
#     def atk(self, value):
#         if 0 <= value <= 50:
#             self.__atk = value
#         else:
#             raise ValueError('攻击力不在区间内')
#
#
# class Enemy:
#     def __init__(self, e_name, e_hp, e_atk):
#         self.e_name = e_name
#         self.e_hp = e_hp
#         self.e_atk = e_atk
#
#     @property
#     def e_hp(self):
#         return self.__e_hp
#
#     @e_hp.setter
#     def e_hp(self, value):
#         if 0 <= value <= 100:
#             self.__e_hp = value
#         else:
#             raise ValueError('血量不在区间内')
#
#     @property
#     def e_atk(self):
#         return self.__e_atk
#
#     @e_atk.setter
#     def e_atk(self, value):
#         if 0 <= value <= 20:
#             self.__e_atk = value
#         else:
#             raise ValueError('攻击力不在区间内')
#
#
#
# p1 = Player('悟空',100,20)
# e1 = Enemy('妖怪',40,10)
#
# #1.玩家(攻击力)攻击敌人(血量)敌人受伤(减血)可能死亡(播放动画)
# print('1.玩家攻击敌人:')
# def p_atk_e():
#     count = 0
#     while True:
#         e1.e_hp -= p1.atk
#         count += 1
#         if e1.e_hp >0:
#             print('玩家攻击%d次,敌人血量减少到%d' %
#                   (count,e1.e_hp))
#         elif e1.e_hp == 0:
#             print('玩家攻击%d次,敌人死亡,播放动画' % count)
#             break
#
# p_atk_e()
#
# # 2.敌人攻击玩家 玩家受伤(减血 碎屏) 可能死亡(游戏结束)
# print('2.敌人攻击玩家:')
# def e_atk_p():
#     count = 0
#     while True:
#         p1.hp -= e1.e_atk
#         count += 1
#         if p1.hp >0:
#             print('敌人攻击%d次,玩家血量减少到%d' %
#                   (count,p1.hp))
#         elif p1.hp == 0:
#             print('敌人攻击%d次,玩家死亡,游戏结束' % count)
#             break
# e_atk_p()


#玩家类
class Player:
    def __init__(self,hp = 100,atk = 100):
        self.hp = hp
        self.atk = atk
    def attack(self,enemy):
        print('电脑:玩家攻击敌人')
        enemy.damage(self.atk)
    def damage(self,value):
        print('玩家:我去')
        #敌人减血
        self.hp -= value
        #可能死亡
        if self.hp <= 0:
            print('敌人:你真菜')

#敌人类
class Enemy:
    def __init__(self,hp = 100,atk = 99):
        self.hp = hp
        self.atk = atk
    def damage(self,value):
        print('敌人:啊')
        #玩家减血
        self.hp -= value
        #可能死亡
        if self.hp <= 0:
            print('电脑:敌人死亡,播放动画')
    def attack(self,player):
        print('电脑:敌人攻击玩家')
        player.damage(self.atk)

p01 = Player()
e01 = Enemy()
p01.attack(e01)
e01.attack(p01)
e01.attack(p01)
