# 2. 字符串  split()  join()  strip() format()
#1.spilt()
# str_1 = input('输入字符串：')
# list_1 = str_1.split(' ')
# print(list_1)
# #2.join()
# str_2 = '-   '.join(list_1)
# print(str_2,type(str_2))

str_1 = 'welcome to xian'
str_1= str_1[::-1]      #naix ot emoclew
print(str_1)
list_1 = str_1.split(' ')    #['naix', 'ot', 'emoclew']
print(list_1)
list_1 = list_1[::-1]         #['emoclew', 'ot', 'naix']
print(list_1)
str_1 = ' '.join(list_1)         #emoclew ot naix
print(str_1)


# #3.strip()
# str_3 = '   hhjkh  '
# str_4 = str_3.strip()
# print(str_4)
#4.格式化字符串的函数 str.format()，
# 它增强了字符串格式化的功能。
# 基本语法是通过 {} 和 : 来代替以前的 %
print('{} is {} years old'.format('cici',20) )
print('{1} is {0} years old'.format('cici',20) )
print('{:<10} is {:>8} years old'.format('cici',20) )
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的