'''
zidian推导式
'''

dic_1 = {}
for i in range(10):
    if i > 5:
        dic_1[i] = i**2
print(dic_1)

dic_1 = {i:i**2 for i in range(10) if i > 5 }
print(dic_1)

dic_1 = {i:i**2 for i in range(10)}
print(dic_1)


