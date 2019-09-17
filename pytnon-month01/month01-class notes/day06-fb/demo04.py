'''
字典
'''
#chuanjianzidian
dic_1 = dict([['name','zhang'],('age',10)])#元素必须在容器里面
print(dic_1)

#tianjiayuansu
#若字典中没有对应键,可以直接添加
dic_1['address'] = "xi'an"
print(dic_1)
#xiugai,对已有的键直接赋值
dic_1['address'] = "li qian"
print(dic_1)

#shanchu,直接删除键

del dic_1['address']
print(dic_1)

#查找字典
# print(dic_1['name'])
# print(dic_1['adress'])#keyerror

if 'name' in dic_1:
    print(dic_1['name'])
if 'address' in dic_1:
    print(dic_1['address'])
print(dic_1.get('adress','查无adress项'))
#获取字典所用元素

for key in dic_1:
    print(key)
    print(dic_1[key])
#huoqujianzhidui
for i in dic_1.items():
    print(i)
for key,value in dic_1.items():
    print(key,value)

#获取键值
for value in dic_1.values():
    print(value)
#嵌套  键不能为可变类型
# dic_2 =