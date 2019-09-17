#列表推导式
list01 = [10,11,3,5,45,9]
list02 = []
list03 = []

list03 = [item + 1  for item in list01 ]
print(list03)
list02 = [item  for item in list01 if item >=10]
print(list02)
list02 = [item + 1  for item in list01 if item >=10]
print(list02)

#列表推导式嵌套:
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 =[]

# for i in list_1:
#     for j in list_2:
#         list_3.append(i + j)
# print(list_3)

list_3 = [i + j for i in list_1 for j in list_2]
print(list_3)

print('列表方法')
# 查找方法:拥有返回值
print('pop',list_3.pop(1))
print('count',list_3.count(8))
print('index',list_3.index(8))

#修改方法:返回值为None
list_3.insert(8,10)  #在索引8插入10
print('insert',list_3)
list_3.sort()
print('sort',list_3)
print('sort',list_3.sort())
list_3.reverse()
print('reverse',list_3)
list_3.remove(10)
print('remove',list_3)
# list_3.clear()
# print('clear',list_3.clear())

# 拷贝方法:拥有返回值
print('copy',list_3.copy())

