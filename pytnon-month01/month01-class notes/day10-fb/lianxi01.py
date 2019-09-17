# list_0= [
#     [0,1,2,3,4],
#     [1,28,45,6,7],
#     [20,7,3,65,2]
# ]
list_0 = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]]
#矩阵转换
def matrix_exchange1():
    list_1= []
    for i in range(len(list_0[0])):
        list_1.append([])
        for j in range(len(list_0)):
            list_1[i].append(list_0[j][i])
def matrix_exchange2(list01):
    for c in range(1,len(list01)):  # 123
        for i in range(c,len(list01)):
            list01[i][c - 1], list01[c - 1][i] = list01[c - 1][i], list01[i][c - 1]

#将所有数字左移,从后往前删除0,再添加0
def zero_delete():
    for i in range(len(list_target)-1,-1,-1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)

#合并
def merge():
    zero_delete()
    for i in range(len(list_target)-1):
        if list_target[i] == list_target[i+1]:
            list_target[i] += list_target[i+1]
            del list_target[i+1]
            list_target.append(0)

#左移:
def move_left():
    for line in list_0:
        global list_target
        list_target = line
        merge()

# move_left()
# print(list_0)

#右移
# def move_right():
#     for i in list_0:
#         i.reverse()
#         move_left()
#         i.reverse()
def move_right():
    for line in list_0:
        global list_target
        # list_target = line[::-1]
        list_target = line
        line.reverse()
        merge()
        line.reverse()
        # line[::-1] = list_target

# move_right()
# print(list_0)
def move_up():
    matrix_exchange2(list_0)
    move_left()
    matrix_exchange2(list_0)

move_up()
print(list_0)














