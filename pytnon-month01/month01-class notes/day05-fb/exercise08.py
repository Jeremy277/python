#浅拷贝
# list_1 = ['三丰','无忌','翠山']
# list_2 = list_1
#
# print(list_1)
#
# list_1[0] = '张三丰'
#
# print(list_1)
# print(list_1[0])
# print(list_2)
# print(list_2[0])

#
# list_1 = [800,900,1000]
# list_2 = list_1
# list_3 = list_1
#
# list_1[0] = 'babai'
# print(list_2)
#
# list_3 = 'jiubai'
# print(list_2)


# list_1 = [800,900,1000]
# list_2 = list_1
# list_1[1] = ['a','b']
# print(list_2)

# list_1 = [800,[900,1000]]
# list_2 = list_1
#
# list_1[1][0] = 200
# print(list_2)

# list_1 = [800,[900,1000]]
# list_2 = list_1.copy()#浅拷贝
# list_1[1][0] = 200
# print(list_2)

# list_1 = [100,200,300]
# list_2 = [100,200,300]
# print(list_2 == list_1)#比较元素与地址无关
# print(list_2 is list_1)#比较地址

# name,sex,age = 'cici','female',18
# print(name)
# print(sex)
# print(age)

list_1 = [100,[200,300]]
list_2 = list_1
list_1[1][0] = 500
print(list_2)


#深拷贝
# import copy
#
# list_1 = [100,[200,300]]
# list_2 = copy.deepcopy(list_1)
# list_1[1][0] = 500
# print(list_1)
# print(list_2)





