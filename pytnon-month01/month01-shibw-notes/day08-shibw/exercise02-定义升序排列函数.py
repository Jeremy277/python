#定义列表升序排序函数(从小到大)
#list01 = [1,5,13,2,4]
#思路
#用第一个元素与后面元素比较 只要发现比第一个小的就换位置
#用第二个元素与后面比较
#...
#用倒数第二个元素与后面比较


# r       0 1 2  3
#        [5,6,13,2,4]  第一遍
#        [2,6,12,5,4]

#        [2,5,12,6,4]
#        [2,4,12,6,5]

#        [2,4,6,12,5]
#        [2,4,5,12,6]

#        [2,4,5,6,12]

#循环的次数 取值 第一个值 第二个值
def mysort(list):
    #len(list)-1 最后一个数据 后面没有值了 不需要再比较
    for r in range(len(list)-1):
        #从当前数据的位置+1(下一个数据)开始 一直比到最后
        for c in range(r+1,len(list)):
            #如果当前数据比后面的数据大 交换位置
            if list[r] > list[c]:
                #a,b = b,a
                list[r],list[c] = list[c],list[r]
list01 = [6,5,13,2,4]
# list01.sort(reverse=True) #[13, 6, 5, 4, 2]
list01.sort(reverse=False) #[2, 4, 5, 6, 13]
print(list01)
list02 = [1,7,2,55,40]
mysort(list02)
print(list02)  #[1, 2, 7, 40, 55]












