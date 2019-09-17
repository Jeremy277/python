#1.list01 = [
#     [0,1,2,3,4],
#     [1,28,45,6,7],
#     [20,7,3,65,2]
# ]
# 根据list01 生成list02
# 要求list02的每一行是list01的每一列
# list02 = [
#     [0,1,20],
#     [1,28,7],
#     ...
# ]

list_1 = [
    [0,1,2,3,4],
    [1,28,45,6,7],
    [20,7,3,65,2]
]
#方法一:
list_2 = []
# count = 0
# row = len(list_1[0])
# col = len(list_1)
# for j in range(row):
#     for i in range(col):
#         list_2.append(list_1[i][j])
# print(list_2)
# for j in range(row):
#     list_2.append(list_2[count:col])
#     count += 3
#     col += 3
# del list_2[:len(list_1[0])*len(list_1) ]
# print(list_2)
#方法二:
# for i in range(len(list_1[0])):
#     list_3 = []
#     for j in range(len(list_1)):
#         list_3.append(list_1[j][i])
#     list_2.append(list_3)
#     # list_2.extend(list_3)
# print(list_2)
#方法三:
for i in range(len(list_1[0])):
    list_2.append([])
    for j in range(len(list_1)):
        list_2[i].append(list_1[j][i])
print(list_2)













