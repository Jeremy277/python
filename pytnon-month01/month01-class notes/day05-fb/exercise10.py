'''
list --> str
'''

list1 = ['a','b','c']
str1 = '+'.join(list1)
print(str1)
print(type(str1))

str_result = ''
for i in range(10):
    str_result += str(i)
print(str_result)


#重点思想: 通过列表拼接字符串
list_4 = []
for i in range(10):
    list_4.append(str(i))

str_result = ''.join(list_4)
print(str_result)

#split
str_2 = '2019-08-06'
list_result = str_2.split('-')
print(list_result)
