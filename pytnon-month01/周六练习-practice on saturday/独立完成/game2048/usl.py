'''
    2048控制台界面
'''
from bll import GameCoreController

class GameConsoleView:
    def __init__(self):
        self.__console = GameCoreController()
    def main(self):
        self.__start()
        self.__update()
    def __start(self):
        self.__console.generate_new_number()
        self.__console.generate_new_number()
        self.__draw_map()
    def __draw_map(self):
        for item in self.__console.map:
            for i in item:
                print(i,end=' ')
            print()
    def __move_map_for_input(self):
            choice = input('请输入选择wsad:')
            if choice == 'w':
                self.__console.move_up()
            elif choice == 's':
                self.__console.move_down()
            elif choice == 'a':
                self.__console.move_left()
            elif choice == 'd':
                self.__console.move_right()
    def __update(self):
        while True:
            self.__move_map_for_input()
            self.__console.generate_new_number()
            self.__draw_map()
            if self.__console.is_game_over():
                print('游戏结束')
                break

