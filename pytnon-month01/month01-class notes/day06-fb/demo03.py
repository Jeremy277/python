'''
元组
'''

tup_1 = ()
print(type(tup_1))#类型元组

list_1 = [1,2,3]
tup_1 = tuple(list_1)
print(type(tup_1))#类型元组

tup_1 = ('20',)
print(type(tup_1))#不加逗号类型为str

tup_1 = ([1,2],3,4)
print(tup_1)

print(tup_1[0][1])

tup_1[0][1] = 2.0
print(tup_1)

