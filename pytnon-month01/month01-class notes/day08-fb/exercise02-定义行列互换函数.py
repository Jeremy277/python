#定义行列互换函数
def row_col(list_1):
    list_2 = []
    for i in range(len(list_1[0])):
        list_2.append([])
        for j in range(len(list_1)):
            list_2[i].append(list_1[j][i])
    return list_2

list_1= [
    [0,1,2,3,4],
    [1,28,45,6,7],
    [20,7,3,65,2]
]
print(row_col(list_1))