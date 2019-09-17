#打印任务信息:
#数据结构:
# [{'name':name, 'age':age, 'sex':sex,
#              'weight':weight}...]
# 方法一
list_1 = []
while True:
    name = input('输入姓名:')
    if name == '':
        print('退出')
        break
    age = int(input('输入年龄:'))
    sex= input('输入性别:')
    weight = float(input('输入体重:'))
    dic_1 = {'name':name, 'age':age, 'sex':sex,
             'weight':weight}
    list_1.append(dic_1)
print(list_1)
for dict_item in list_1:
    print('%s的年龄是%d,性别是%s,体重是%.1f' % (dict_item['name'],
          dict_item['age'],dict_item['sex'],dict_item['weight']))

#方法二
# list_1 = []
# dic_1 ={}
# while True:
#     dic_1['name'] = input('输入姓名:')
#     if dic_1['name'] == '':
#         print('退出')
#         break
#     dic_1['age'] = int(input('输入年龄:'))
#     dic_1['sex']= input('输入性别:')
#     dic_1['weight'] = float(input('输入体重:'))
#     list_1.append(dic_1)
# print(list_1)
# for dict_item in list_1:
#     print('%s的年龄是%d,性别是%s,体重是%.1f' % (dict_item['name'],
#           dict_item['age'],dict_item['sex'],dict_item['weight']))

