#宠物养成游戏
#1.pet类 name hunger boredom
class Pet:
    def __init__(self,name,hunger = 0,boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
#2.时间流逝方法 pass_time
    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1
#3.心情方法 mood
    @property
    def mood(self):
        mood_value = self.hunger + self.hunger
        if 0 <= mood_value <= 5:
            mood_ = '开心心!'
        elif 6 <= mood_value <= 10:
            mood_ = '一般般!'
        else:
            mood_ = '哭唧唧!'
        return mood_
#4.talk()
    def talk(self):
        print('你的%s小宝贝来了,我现在心情%s!' % (self.name,self.mood))
        self.__pass_time()
#5.eat()
    def eat(self,food = 4):
        print('吃饱啦,^-^!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
#6play()
    def play(self,fun = 4):
        print('好有趣,*_*!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
#7.主程序
def main():
    pet_name = input('你想要给你的宠物起什么名字呢?\n')
    pet = Pet(pet_name)
    choice = None
    while choice != '0':
        print('''
        ********************
            宠物养成游戏
           0-退出
           1-听听宠物的心声
           2-给宠物喂吃的
           3-陪宠物玩
        ********************
        ''')
        choice = input('请选择:\n')
        if choice == '0':
            print('谢谢,退出游戏!')
        elif choice == '1':
            pet.talk()
        elif choice == '2':
            pet.eat()
        elif choice == '3':
            pet.play()
        else:
            print('请正确输入选项!')


main()
input('\n\n按回车键退出!')
