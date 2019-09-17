l1 = [0,1,2,3,1]
#
# print(l1.index(1))
# print(l1.count(1))
# # l1.pop([1])
# print(l1)
# #添加
# l1.append(4)
# print(l1)
# for i in range(5,8):
#     l1.append(i)
# print('app',l1)
# l1.extend(range(5,8))
# print(l1)
# #插入
# l1.insert(0,0)
# print(l1)

# str1 = ' hell o '
# # print(str1.lstrip())
# # print(str1.rstrip())
# # print(str1.strip())
# print(str1)
# print(str1.lstrip(' h'))
# print(str1.rstrip('o '))



# list01 = []
# # list(可迭代对象) 使用可迭代对象快速创建列表
# list01 = list()
# print(list01)

# # #具有值的列表
list02 = ['shibw',18,True,[1,2,3]]
# print(list02)
# list02 = list(range(4))
# print(list02)
# list02 = list("我是小妖怪")
# print(list02)

for i in range(5,8):
    list02.append(i)
print(list02)
