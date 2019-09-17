#冒泡排序

list_ = [56,2,6,98,12,45,7,9]

def sort_1(list_1):
    for i in range(len(list_1)-1):
        for j in range(i+1,len(list_1)):
            if list_1[i] > list_1[j]:
                list_1[i],list_1[j] = list_1[j],list_1[i]

sort_1(list_)
print(list_)