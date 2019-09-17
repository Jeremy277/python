# len(x)
# 返回序列的长度
# max(x)
# 返回序列的最大值元素
# min(x)
# 返回序列的最小值元素
# sum(x)
# # 返回序列中所有元素的和(元素必须是数值类型)
# l = [1,2,3,4]
# print(len(l))
# print(max(l))
# print(min(l))
# print(sum(l))

#1.猜数字：

# import random
#
# c = random.randint(1,100)
# print(c)
# while True:
#     y = int(input('我准备好了，请猜:'))
#     if y == c:
#         print('猜对了')
#         break
#     elif y > c:
#         print('猜大了')
#     else:
#         print('猜小了')

#2.猜数字，猜三次，之后报错
import random

c = random.randint(1,100)
count = 1
print(c)
# while count <= 3:
for i in range(3):
    y = int(input('我准备好了，请猜:'))
    if y == c:
        count += 1
        print('猜对了！')
        break
    elif y > c:
        count += 1
        print('猜大了！')
    else:
        count += 1
        print('猜小了！')
else:
    print('您猜了三次没有猜对！')

#3.在1-100之间给定数字，电脑来猜，直到猜对为止。
# import random
#
# y = int(input('\33[34m电脑要猜的数字（1-100）：\33[0m'))
# i = 1
# j = 100
# n = 0
#
# if 1 <= y <= 100:
#     while True:
#         c = random.randint(i,j)
#         if c == y:
#             print('\33[31m电脑猜了%d次，正确数字是%d。\33[0m' % (n,c))
#             break
#         elif c > y:
#             print('\33[32m猜大了\33[0m', c ,'。')
#             j = c
#             n += 1
#         else:
#             print('\33[33m猜小了\33[0m', c ,'。')
#             i = c
#             n +=1
# else:
#     print('输入数字超范围。')
