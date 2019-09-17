#1.输入输出
# print('hi','cici',sep='')
# num = input('请输入:')
# print(type(num))#input获得的数据是字符型
# #2.密码
# import getpass##注，此模块在pycharm中无法使用。
##
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
print('%s is %5.2f years old' % ('cici',15.5))#%5.2f是宽度为5,2位小数
print("97 is %c"% 97)#转化为ASCII
print("11 is %#o" % 11)#11 is 0o13
print('11 is %#x' % 11)#11 is 0xb
print('%8s%2s' % ('name','age'))#%10s表示总宽度是10,右对齐
print('%10s%5s' % ('name',23))
print('%-5s%-5s' % ('name','age'))
print('%-10s%-10s' % ('name',23))#%-10s表示总宽度是10,左对齐
print('{} is {} years old'.format('cici',20) )
print('{1} is {0} years old'.format('cici',20) )
print('{:<10} is {:>8} years old'.format('cici',20) )#<左对齐 >右对齐(宽度为10)
# str.format()，它增强了字符串格式化的功能。
# 基本语法是通过 {} 和 : 来代替以前的 % 。
# format 函数可以接受不限个参数，位置可以不按顺序。
#11.列表方法:
list_1 = [1,2,3,'coco','cici']
list_1[1:3] = [20,30]#[1, 20, 30, 'coco', 'cici']
print(list_1)
list_1[2:2] = [22,33,44]#[1, 20, 22, 33, 44, 55, 30, 'coco', 'cici']
print(list_1)
list_1[:7] = []
list_1.append('jer')#['coco', 'cici', 'jer']
print(list_1)
list_1.extend('jer')#['coco', 'cici', 'jer', 'j', 'e', 'r']
print(list_1)
list_1.extend(['hello','nihao'])
print(list_1)
#12.动画程序:@从一行中#穿过
#\r是回车不换行
# import time
# length = 19
# count = 0
# while True:
#     print('\r%s@%s' % ('#' * count,'#' * (length - count)),end='')
#     try:
#         time.sleep(0.3)
#     except KeyboardInterrupt:
#         print('\nBye-bye')
#         break
#     if count == length:
#         count = 0
#     count += 1
#13.字典基础用法:
adict = dict()   #{}
dict(['ab','cd'])#{'a': 'b', 'c': 'd'}
bdict = dict([('name','cici'),('age',18)])#{'name': 'cici', 'age': 18}
{}.fromkeys(['zhangsan','lisi','wangwu'],11)
#{'zhangsan': 11, 'lisi': 11, 'wangwu': 11}
#fromkeys() 函数用于创建一个新字典，以序列 seq 中元素做字典的键，
# value 为字典所有键对应的初始值
print(bdict.pop('age'))#删除键值,并返回值
bdict.clear()#清空
# 14.字典常用方法
adict = dict([('name','cici'),('age',18)])
print(len(adict))#2
print(hash(1))#判断给定数据是不是不可变的,不可变数据才能作为key
print(adict.keys())
print(adict.values())
print(adict.items())
print(adict.get('name'))
adict.update({'phone':'13572093824','sex':'female'})#字典记录累加
print(adict)
#15.集合常用方法:集合相当于无值的字典
set_1 = set('hello')
print(len(set_1))
for ch in set_1:#不重复 不可变 无序
    print(ch)
aset = set('abc')
bset = set('cde')
print(aset.intersection(bset))#交集  &  {'c'}
print(aset.union(bset))#并集  |
print(aset.difference(bset))#并集  aset-bset  {'b', 'd', 'e', 'a', 'c'}
aset.add('new')#{'b', 'new', 'a', 'c'}  {'b', 'a'}
aset.update(['aaa','bbb'])#{'c', 'a', 'bbb', 'new', 'b', 'aaa'}
aset.remove('bbb')#{'c', 'new', 'aaa', 'b', 'a'}
cset = set('abcde')
dset = set('bcd')
print(cset.issuperset(dset))#True cset是dset的超集吗
print(cset.issubset(dset))#False  cset是dset的子集吗
#16.计算千万次加法运算时间
import time
result = 0
start = time.time()#返回运算前时间戳
for i in range(10000000):
    result += i
end = time.time()#返回运算后时间戳
print(result)
print(end - start)







