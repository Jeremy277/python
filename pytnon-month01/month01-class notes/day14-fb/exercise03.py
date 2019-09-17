class Enemy:
    def __init__(self,name='',hp=0,atk=0):
        self.name = name
        self.hp = hp
        self.atk = atk
    # def __str__(self):
    #     return '%s %d %d' % (self.name,self.hp,self.atk)
    def __repr__(self):
        return 'Enemy("%s",%d,%d)' % (
            self.name,self.hp,self.atk
        )


e01 = Enemy('灭霸',5000,1000)
print(e01)

e02 = eval(repr(e01))
e02.name = '黑豹'
print(e02)
print(e01)

