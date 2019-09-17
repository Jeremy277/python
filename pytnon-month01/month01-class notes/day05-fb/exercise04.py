l1 = ['a','b','c']
# print(l1)
# print('前两个元素:',l1[0:2])
#赋值,修改为4个元素
l1[0:2] = [0,1,2]
# print(l1)

l1[:3] = []
# print(l1)

l2 = [0,1,2,3,4]
#获取列表所有元素
# for i in l2:
    # print(i)

#删除
list3 = [1,2,3,4,5]
list3.remove(4)
print(list3)#根据元素
del list3[1]
print(list3)#根据索引