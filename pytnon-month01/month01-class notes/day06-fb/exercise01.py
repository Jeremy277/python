# #1.生成1-10列表,平方后放入列表

list01 = list(range(1,11))
list02 = []
list03 = []
list04 = []

print(list01)

list02 = [i ** 2 for i in list01 ]
print('平方',list02)

list03 = [i for i in list01 if i % 2]
print('奇数',list03)

list04 = [i + 10 for i in list01 if not i % 2]
print('偶数加10',list04)


