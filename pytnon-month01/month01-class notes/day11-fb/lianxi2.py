class Critter:
    def __init__(self,name):
        print('小动物出生了!')
        # self.__name = name
        self.name = name

    @property
#如果需要对私有对象进行访问,习惯做法是
# 将私有特性名称前的下划线去掉,并以此为属性名
    def name(self):
        return self.__name
    @name.setter
#通过属性name对私有特性_name进行写入访问
    def name(self,new_name):
        if new_name == '':
            # print('小动物的名字不能为空!')
            raise ValueError('超过范围')
        else:
            self.__name = new_name
            print('命名成功!')
    def talk(self):
        print('你好呀,我是' + self.name)
#创建对象
crit = Critter(' ')
crit.talk()
#
# print(crit.name)
# #修改对象
# crit.name = '雪梨'
# print(crit.name)

#修改对象为空
crit.name = ''
print(crit.name)




