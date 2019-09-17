'''
2048核心算法
'''
game_map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]
#1.从后往前删除零元素 先删除在补零
def zero_delete(list_target):
    for item in range(len(list_target)-1,-1,-1):
        if list_target[item] == 0:
            del list_target[item]
            list_target.append(0)
# list_1 = [2,0,0,2]
# zero_delete(list_1)
# print(list_1)

#2.合并,相邻两个元素相等,相加,在补0
def merge(list_target):
    zero_delete(list_target)
    for item in range(len(list_target)-1):
        if list_target[item] == list_target[item+1]:
            list_target[item] += list_target[item + 1]
            del list_target[item + 1]
            list_target.append(0)

# merge(list_1)
# print(list_1)

#3.左移 将每一列元素取出 进行合并
def move_left():
    for line in game_map:
        merge(line)

# move_left()
# print(game_map)

#4.右移 ,将每一列元素取出,反转 ,左移,反转
def move_right():
    for line in game_map:
        line.reverse()
        merge(line)
        line.reverse()
# move_right()#[[0, 0, 0, 4], [0, 0, 8, 4], [0, 0, 2, 8], [0, 0, 0, 4]]
# print(game_map)
# def move_right():
#     for line in game_map:
#         # global list_target
#         list_target = line[::-1]
#         merge(list_target)
#         line[::-1] = list_target
move_right()#[[0, 0, 0, 4], [0, 0, 8, 4], [0, 0, 2, 8], [0, 0, 0, 4]]
print(game_map)

#5.上移,先将矩阵行列互换,再左移,再矩阵行列互换
#矩阵转换:
# def square_matrix():
#     list_1 = []
#     for i in range(len(game_map[0])):
#         list_1.append([])
#         for j in range(len(game_map)):
#             list_1[i].append(game_map[j][i])
#     return list_1
def square_matrix():
    for r in range(1,len(game_map)):
        for c in range(r,len(game_map)):
            game_map[c][r-1],game_map[r-1][c] = game_map[r-1][c], game_map[c][r-1]

# square_matrix()
# print(game_map)

#上移
def move_up():
    square_matrix()
    move_left()
    square_matrix()

# move_up()#[[2, 8, 4, 4], [4, 0, 0, 4], [2, 0, 0, 2], [0, 0, 0, 0]]
# print(game_map)

# 下移,先将矩阵行列互换,再右移,再矩阵行列互换
def move_down():
    square_matrix()
    move_right()
    square_matrix()

# move_up()#[[2, 8, 4, 4], [4, 0, 0, 4], [2, 0, 0, 2], [0, 0, 0, 0]]
# print(game_map)
# move_down()#[[0, 0, 0, 0], [2, 0, 0, 4], [4, 0, 0, 4], [2, 8, 4, 2]]
# print(game_map)








