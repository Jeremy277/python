#三行五列的二维列表:
list_1 = [[0,1,2,3,4],
          [1,56,89,2,41],
          [20,5,6,3,89]]

# for i in list_1[1]:
#     print(i,end=' ')
#
# print()
#
# for i in range(len(list_1)):
#     print(list_1[i][0],end=' ')
#
# print()

# for i in range(len(list_1)):
#     for j in range(len(list_1[i])):
#         print(list_1[i][j],end=' ')
#     print()
# for i in range(len(list_1)):
#     for j in list_1[i]:
#         print(j,end=' ')
#     print()

#练习,行列互换
list_2 = []
count = 0
row = len(list_1[0])
col = len(list_1)
for j in range(row):
    for i in range(col):
        list_2.append(list_1[i][j])
print(list_2)
for j in range(row):
    list_2.append(list_2[count:col])
    count += 3
    col += 3
del list_2[:len(list_1[0])*len(list_1) ]
print(list_2)
