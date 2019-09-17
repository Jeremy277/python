#将列表中大于10的数,存入另一个列表

list_1 = [3,56,2,6,89,12,45,9,58,3,5]
list_2 = []
list_3 = []

print(list_1)
for i in list_1:
    if i > 10:
        list_2.append(i)
print(list_2)

#输出最大值,不适用max函数
max_ = list_1[0]
# for j in list_1[1:]:
#     if j > max_:
#         max_ = j

#这样写效率最高:
for i in range(1,len(list_1)):
    if list_1[i] > max_:
        max_ = list_1[i]

print('max:',max_)

#删除奇数:

# for i in list_1:
#     if  not i % 2:
#         list_3.append(i)
# print(list_3)

#正序删除存在本质问题,列表地址自动向前进位
for i in list_1:
    if i % 2:
        list_1.remove(i)
print('li',list_1)

#反向删除无此问题
for i in range(len(list_1)-1,-1,-1):
    # print(list_1[i],end=' ')
    if  list_1[i] % 2:
        del list_1[i]
        # list_1.remove(list_1[i])

print(list_1)


l_3 = [1,2,3,4,5]

for i in l_3:
    l_3.remove(i)
print(l_3)





