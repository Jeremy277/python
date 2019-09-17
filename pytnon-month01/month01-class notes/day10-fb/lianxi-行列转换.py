#方法一:任意矩阵
game_map = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12,],
    [13,14,15,16]]

list_1 = []
for i in range(len(game_map[0])):
    list_1.append([])
    for j in range(len(game_map)):
        list_1[i].append(game_map[j][i])
print(list_1)

#方法二:只能为方阵
list_2 = [
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    [4,8,12,16]]

for c in range(1,len(game_map)):
    for i in range(c,len(game_map)):
        game_map[i][c-1],game_map[c-1][i] = \
           game_map[c-1][i],game_map[i][c-1]
print(game_map)

#list_1[1][0] --> list_2[0][1]
#list_1[2][0] --> list_2[0][2]
#list_1[3][0] --> list_2[0][3]
# for i  in range(1,4):
#     list_1[i][0] = list_1[0][i]
# #list_1[2][1] --> list_2[1][2]
# #list_1[3][1] --> list_2[1][3]
# for i  in range(2,4):
#     list_1[i][1] = list_1[1][i]
# #list_1[3][2] --> list_2[2][3]
# for i  in range(3,4):
#     list_1[i][2] = list_1[2][i]
