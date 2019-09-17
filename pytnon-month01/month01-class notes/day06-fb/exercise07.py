#1.
list_1 = ['张三丰','翠山','无忌']
dict_1 = {}

list_1.reverse()

for key in list_1:
    dict_1[key] = len(key)
print(dict_1)

dict_1 = {key:len(key) for key in list_1}
print(dict_1)

#2.
list_h = ['无忌','赵敏','周芷若']
list_n = ['101','102','103']
dict_2 = {}

for key in list_h:
    dict_2[key] = list_n[list_h.index(key)]
print(dict_2)


# for i in range(len(list_h)):
#     dict_2[list_h[i]] = list_n[i]
# print(dict_2)

dict2 = {key:list_n[list_h.index(key)] for key in list_h}
print(dict_2)
#方法一:两个字典合并
# dict_4 = dict(dict_1.items()+dict_2.items())
print(dict_2.items())
#方法二:两个字典合并  下述效率高
dict_3 = dict(dict_1,**dict_2)
dict_4 = dict_1.copy()
dict_4.update(dict_2)
print(dict_3)
print(dict_4)

print(dict_2.popitem())
print(dict_2)
dict_2.clear()
print(dict_2)
