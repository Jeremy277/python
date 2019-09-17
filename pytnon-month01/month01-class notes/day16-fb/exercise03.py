#敌人类
class AtkError(BaseException):
    def __init__(self,id,code,message):
        self.message = message
        self.code = code
        self.id = id

class Enemy:
    def __init__(self,name,atk):
        self.name = name
        self.atk = atk
    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise AtkError(101,'0 <= atk <= 100',
                           '攻击力不在范围',)

try:
    e01 = Enemy('洛阳',500)
    print(e01.name,e01.atk)
except AtkError as e:
    print(e.id,e.code,e.message,e.code)#101 0 <= atk <= 100 攻击力不在范围 0 <= atk <= 100
    print(e.args)#(101, '0 <= atk <= 100', '攻击力不在范围')
