# 1.在控制台循环录入字符串 如果录入的是空字符串 退出循环
#  打印所有录入的内容

# #空列表 保存数据
# str_list = []
# #循环添加数据到空列表
# while True:
#     str_1 = input('请输入字符：')
#     if str_1 == '':
#         break
#     str_list.append(str_1)
# #打印列表的每一个元素
# str_1 = '\n'.join(str_list)
# print(str_1,end=' ')

# 2.通过列表的方式模拟斐波那契数列
# 斐波那契数列特点 每一个值都是前两个数相加的结果
#  0 1 1 2 3 5 8 13 ...
#
# fibs = [0,1]
# 打印前15个斐波那契数列


# #方法一：
a = 0
b = 1
for i in range(15):
    print(b,end=' ')
    a,b = b,a+b  #变量交换a=1,b=1
print('\n')
#
# a = 0
# b = 1
# while b < 15:
#     print(b,end=' ')
#     a = b        #a=1,b=1
#     b = a+b      #a=1,b=2

#方法二：
list_1 = []

for i in range(15):
    if i == 0 or i == 1:
        list_1.append(1)
    else:
        list_1.append(list_1[-2] + list_1[-1])
print(list_1)
#
# #方法三(*没看懂)
def fab(n):
    if n == 1 or n == 2:
        # print(1,end=' ')
        return 1
        # return print(1,end=' ')
    else:
        # print(fab(n))
        return fab(n-1) + fab(n-2)
        # return print(fab(n-1) + fab(n-2),end=' ')

res = fab(5)
print(res)



