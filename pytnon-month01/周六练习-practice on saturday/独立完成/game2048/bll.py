'''
    2048算法
'''
from model import Location
import random
class GameCoreController:
    def __init__(self):
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.__list_line = None
        self.__list_empty = []
    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        '''将0元素移动到末尾'''
        for i in range(len(self.__list_line)-1,-1,-1):
            if self.__list_line[i] == 0:
                del self.__list_line[i]
                self.__list_line.append(0)

    def __merge(self):
        '''合并'''
        self.__zero_to_end()
        for i in range(len(self.__list_line)-1):
            if self.__list_line[i] == self.__list_line[i+1]:
                self.__list_line[i] += self.__list_line[i+1]
                del self.__list_line[i+1]
                self.__list_line.append(0)
    def move_left(self):
        '''左移'''
        for line in self.__map:
            self.__list_line = line
            self.__merge()
    def move_right(self):
        '''右移'''
        for line in self.__map:
            line.reverse()
            self.__list_line = line
            self.__merge()
            line.reverse()
    def __Square_matrix_conversion(self):
        '''方阵转换'''
        for r in range(len(self.__map)-1):
            for c in range(r+1,len(self.__map)):
                self.__map[c][r],self.__map[r][c] =\
                    self.__map[r][c],self.__map[c][r]
    def move_up(self):
        '''上移'''
        self.__Square_matrix_conversion()
        self.move_left()
        self.__Square_matrix_conversion()
    def move_down(self):
        '''下移'''
        self.__Square_matrix_conversion()
        self.move_right()
        self.__Square_matrix_conversion()
    def generate_new_number(self):
        '''生成新数字'''
        self.__get_empty_location()
        if len(self.__list_empty) == 0:
            return
        loc = random.choice(self.__list_empty)
        self.__map[loc.r_index][loc.c_index] = self.__select_number()
        self.__list_empty.remove(loc)

    def __get_empty_location(self):
        self.__list_empty.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty.append(Location(r,c))
    def __select_number(self):
        return 4 if random.randint(1,10)==1 else 2

    def is_game_over(self):
        '''游戏是否结束'''
        if len(self.__list_empty)>0:
            return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])-1):
                if self.__map[r][c] == self.__map[r][c+1] or\
                    self.__map[c][r] == self.__map[c+1][r]:
                    return False
        return True



#测试代码
if __name__ == '__main__':
    console = GameCoreController()
    # console.move_right()
    # console.move_left()
    # console.move_up()
    console.move_down()
    print(console.map)