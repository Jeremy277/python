#创建敌人类
#给血量(1-100) 攻击力(1-50)
class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp = hp
        self.atk = atk
    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self,set_hp):
        if 1 <= set_hp <= 100:
            self.__hp = set_hp
        else:
            raise ValueError('血量不在范围')
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self, set_atk):
        if 1 <= set_atk <= 50:
            self.__atk = set_atk
        else:
            raise ValueError('攻击力不在范围')

e01 = Enemy('灭霸',10,1)
print(e01.name)
print(e01.hp)
print(e01.atk)
e01.hp = 100
print(e01.hp)





