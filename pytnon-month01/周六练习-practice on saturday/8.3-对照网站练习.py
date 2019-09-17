# 1.企业奖金发放
# i = int(input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print ((i-arr[idx])*rat[idx])
#         i=arr[idx]
# print (r)
# 2.输入三个整数x,y,z，请把这三个数由小到大输出。
#方法一：
# list_1 = []
#
# for i in range (3):
#     list_1.append(int(input('请依次输入三个数字：')))
#
# print('输入的三个数字依次为：',list_1)
# list_1.reverse()
#
# print(list_1)
#
# list_1.sort()
#
# print('按从小到大输出为：',list_1)

#方法二：
num_1 = int(input('输入第一个数字：'))
num_2 = int(input('输入第二个数字：'))
num_3 = int(input('输入第三个数字：'))
num_min = num_1
# num_mid = num_2
num_max = num_3

if num_min > num_2:
    num_min = num_2
if num_min > num_3:
    num_min = num_3

if num_max < num_1:
    num_max = num_1
if num_max < num_2:
    num_max = num_2

if num_1 != num_max and num_1 != num_min:
    num_mid = num_1
elif num_2 != num_max and num_2 != num_min:
    num_mid = num_2
else:
    num_mid = num_3

print(num_min,num_mid,num_max)

#3. 输出斐波那契数列

def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a

num = int(input('需要输出第几个数列：'))

print (fib(num))

# 4.将一个列表的数据复制到另一个列表中。
# a = (1,2,3)#元组
# b = a[:]
#
# print(b)
#
# a = [1,2,3]#列表
# b = a[:]
#
# print(b)

# 5.
print('输出 9*9 乘法口诀表')
for i in range(1,10):
    for j in range(1,i + 1):
        num = i * j
        print('%d*%d=%d'% (i,j,num),end = ' ')
    print('')
#6.
print('暂停1秒输出')
import time

dic = {'男':'张三 李四','女':'貂蝉''西施'}
#调用字典
print(dic['男'])
#通过get()调用字典
print(dic.get('就','查无此项'))
print(dic.get('男','查无此项'))
#显示字典所有 键 值 项
print(dic.values())
print(dic.keys())
print(dic.items())
#增加字典
shiyi = input('请输入新加项：')
dic['不男不女'] = shiyi
print(dic.items())
#修改字典
dic['不男不女'] = '小猫'
print(dic.items())
#删除字典
del dic['不男不女']
print(dic.items())

for sex,name in dic.items():

    print(sex,name)
    time.sleep(1)

#7.兔子的规律为数列1,1,2,3,5,8,13,21....问每个月的兔子总数为多少？

# f1 = 1
# f2 = 1
# for i in range(1,22):
#     print ('%10d %10d' % (f1,f2))
#     if (i % 3) == 0:
#         print ('')
#     f1 = f1 + f2
#     f2 = f1 + f2

#8.判断101-200之间有多少个素数，并输出所有素数。

# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，
#  如果能被整除，则表明此数不是素数，反之是素数。
# leap = 1
# # from math import sqrt
# import math
# for m in range(101,201):
#     for i in range(2,int(math.sqrt(m) + 1)):
#         if m % i == 0:
#             leap = 0
#             break
#
#     if leap == 1:
#         print(m)
#
#     leap = 1

# 9.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import  string
# print(string.punctuation)
# print(dir(string))
# str1 = input('qinsghuruzifu:')
# letter = 0
# space = 0
# digit = 0
# others = 0
#
# for c in str1:
#     if c.isalpha():
#         letter += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
#
# print ('char = %d,space = %d,digit = %d,others = %d' % (letter,space,digit,others))
#

#10.题目：
print('求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。')
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
a = int(input('a='))
n = int(input('n='))
num = 0
sum_ = 0
l=[]

for i in range(1,n + 1):
    num += a
    a *= 10
    l.append(num)
    print(num)
print(l)
print('调用sum函数:',sum(l))

# for i in range(len(l)):
#     print(i,l[i])
#     sum_ += l[i]
# print(sum_)
for i in l:
    print(l.index(i),i)
    sum_ += i
print('遍历元素相加：',sum_)
# 11.输出如下图形
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

from sys import stdout

for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print (' ')

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print (' ')
# 12. 获取 100 以内的质数。
num=[]
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)









































































