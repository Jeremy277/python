#手雷炸了 伤害敌人/玩家的生命
#还有可能伤害未知生命(动物\花草...)
#增加事物时 不影响手雷

#手雷
class Grenade:
    def __init__(self,atk=100):
        self.atk = atk
    def attack(self,victim):
        if not isinstance(victim, Victim):
            raise ValueError('目标对手雷免疫')
        print('开始手雷攻击')
        victim.damage(self.atk)

#从子类  抽象类
class Victim:
    def damage(self,value):
        raise NotImplementedError('如果子类不重写则异常')

#抽象代码
#-------------------------------------------
#具体代码

#敌人
class Enemy(Victim):
    def __init__(self,hp=100):
        self.hp = hp

    def damage(self,value):
        print('敌人减血')
        self.hp -= value
        if self.hp <= 0:
            print('敌人死了')
#玩家
class Player(Victim):
    def __init__(self, hp=101):
        self.hp = hp

    def damage(self, value):
        print('玩家减血')
        self.hp -= value
        if self.hp <= 0:
            print('玩家死了')
#小动物
class Critter(Victim):
    def __init__(self, hp=20):
        self.hp = hp

    def damage(self, value):
        print('小动物减血')
        self.hp -= value
        if self.hp <= 0:
            print('小动物死了')


g01 = Grenade()
e01 = Enemy()
c01 = Critter()
p01 = Player()

g01.attack(e01)
g01.attack(p01)
g01.attack(p01)
g01.attack(c01)
