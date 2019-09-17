#定义列表升序排列函数

def a(list):
    for r in range(len(list)-1):
        for c in range(r+1,len(list)):
            if list[r] > list[c]:
               list[r] ,list[c] = list[c],list[r]
    return list

list_1 = [6, 5, 13, 2, 4]
print(a(list_1))


