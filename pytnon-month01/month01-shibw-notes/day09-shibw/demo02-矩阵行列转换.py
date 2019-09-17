# list_1 = [2,4,3,1]
# print(list_1[::-1])
# list_1.reverse()
# print(list_1)

#矩阵转换
list_1 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
list_2 = [
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    [4,8,12,16]]
#      5      -->       2
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
#
for c in range(1,4):
    for i in range(c,4):
        list_1[i][c-1],list_1[c-1][i] = \
            list_1[c-1][i],list_1[i][c-1]
print(list_1)

