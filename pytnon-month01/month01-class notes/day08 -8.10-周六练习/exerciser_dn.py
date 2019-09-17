#1.输入输出
# print('hi','cici',sep='')
# num = input('请输入:')
# print(type(num))#input获得的数据是字符型
# #2.密码
# import getpass
#
# user_name = input('username:')
# password = getpass.getpass('password:')
# if user_name == 'you' and password == '123456':
#     print('成功')
# else:
#     print('失败')
#3.fib
fib = [0,1]
for i in range(8):
    fib.append(fib[-1]+fib[-2])
print(fib)
#4.
print('输出 9*9 乘法口诀表')
for i in range(1,10):
    for j in range(1,i + 1):
        num = i * j
        print('%d*%d=%d'% (i,j,num),end = ' ')
    print('')
#6.逐步实现列表解析
result = [10 + 5]
print(result)
result = [10 + 5 for i in range(10)]
print(result)
result = [10 + 5 for i in range(10) if i % 2]
print(result)
# result = ['192.168.1.%s' % i for i in range(4)]
# print(result)
#7.序列对象方法一
print(result[0])
result = str(result)
print(result)
print(result[0])#列表从中括号起都是字符串
# print(type(result))
#8.序列对象方法二:
list_1 = [10,'john']
for i in range(len(list_1)):
    print('%s:%s' % (i,list_1[i]))
for i in enumerate(list_1):
    print('%s:%s' % (i[0],i[1]))
for i,j in enumerate(list_1):
    print('%s:%s' % (i,j))
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
# 组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
tuple_1 = (45,87,12,4,556,89,14,125,85,3,2,21)
print(sorted(tuple_1,reverse=True))
# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
# 语法
# sorted 语法：
# sorted(iterable, cmp=None, key=None, reverse=False)
#9.字符串方法
str_1 = '   hello cici'
print(str_1.capitalize())#首字母大写
print(str_1.title())  #所有单词首字母大写,其余字母小写
print(str_1.center(20))
print(str_1.center(20,'#'))#####helo cici######
print(str_1.count('l'))
print(str_1.endswith('i'))
print(str_1.strip())
print('how/are/you'.split())
print('how/are/you'.split('/'))
print('$'.join(['hello','cici','jer']))
#10.字符串格式化
