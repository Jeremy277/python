#1.
l = [4,5,7,1,2,9,6,8]
def mysort(list):
    count = 0
    #len(list)-1 最后一个数据 后面没有值了 不需要再比较
    for r in range(len(list)-1):
        #从当前数据的位置+1(下一个数据)开始 一直比到最后
        for c in range(r+1,len(list)):
            count += 1
            #如果当前数据比后面的数据大 交换位置
            if list[r] > list[c]:
                #a,b = b,a
                list[r],list[c] = list[c],list[r]
    return count
print(mysort(l))
print(l)

count = 0
for r in range(7):
    # 从当前数据的位置+1(下一个数据)开始 一直比到最后
    for c in range(7-r):
        count += 1
    print(count)