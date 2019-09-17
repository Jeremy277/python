#创建敌人类
#给血量(1-100) 攻击力(1-50)
class Enemy:
    def __init__(self,name,hp,atk):
        self.name = name
        self.set_enemy(hp,atk)

    def get_enemy(self):
        return self.name,self.__hp,self.__atk

    def set_enemy(self,set_hp,set_att):
        if 1 <= set_hp <= 100:
            self.__hp = set_hp
        else:
            raise ValueError('血量不在范围')
        if 1 <= set_att <= 50:
            self.__atk = set_att
        else:
            raise ValueError('攻击力不在范围')

e01 = Enemy('灭霸',10,1)
print(e01.get_enemy())
# print(e01.hp)#报错'Enemy' object has no attribute 'hp'
