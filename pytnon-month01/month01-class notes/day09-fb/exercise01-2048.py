# list_1 = [
#     [2,0,2,0],
#     [2,2,0,0],
#     [4,2,4,2],
#     [4,4,0,0]
# ]
# list_target = []
# [0,4,0,0] --> [4,0,0,0]
# [0,0,2,0] --> [2,0,0,0]

#1.去除列表中非零数字,放入新列表,在判断源列表有多少零,添加进新列表
#方法一:
# def zero_end(list_target):
    # new_list = []
    # for item in list_target:
    #     if item != 0:
    #         new_list.append(item)
    #列表推导式:
    # new_list = [item for item in list_target if item  != 0]

    # for i in  range(li
    #extend
    # new_list.extend([0] * list_target.count(0))
    # new_list += [0] * list_target.count(0)


    # return new_list

# print(zero_end([0,0,4,0]))

#方法二:

# 1.先删除0元素,再添加0元素:

#1.思路从后往前删:若为0 删除 再添加
def zero_to_end():
    for i in range(len(list_target)-1,-1,-1):
        if list_target[i] == 0:
            # list_target.remove(list_target[i])
            del list_target[i]
            list_target.append(0)

# print(zero_to_end([2,0,2,0]))

#2.合并 先将0元素移动到末尾 ,在合并相邻的元素
#如果相邻元素相同,合并 ,在补0
def merge():
    zero_to_end()
    for item in range(len(list_target)-1):
        if list_target[item] == list_target[item+1]:
            list_target[item] += list_target[item+1]
            del list_target[item + 1]
            list_target.append(0)

game_map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]
#3.左移
#将二维列表中的每一个列表取出,交给merge函数操作
def move_left():
    for line in game_map:
        global list_target
        list_target = line
        merge()

#4.右移(从右向左接受数据)
#   原始列表    先反转     合并左移   再反转
# [4,4,2,2] [2,2,4,4] [4,8,0,0] [0,0,8,4]
def move_right():
    for line in game_map:
        global list_target
        list_target = line
        # list_target = line[::-1]
        line.reverse()
        merge()
        line.reverse()
        # line[::-1] = list_target
move_right()
print(game_map)

#5.上.下移动

#第一步:将矩阵行列转换
def square_matrx(list_1):
    for c in range(1,len(list_1)):
        for i in range(c,len(list_1)):
            list_1[i][c - 1], list_1[c - 1][i] = \
                list_1[c - 1][i], list_1[i][c - 1]
#第二步:此时上移相当于左移
def move_up():
    square_matrx(game_map)
    move_left()
    square_matrx(game_map)
#第三步:此时下移相当于右移
def move_down():
    square_matrx(game_map)
    move_right()
    square_matrx(game_map)

move_up()
print(game_map)
# move_down()
# print(game_map)





