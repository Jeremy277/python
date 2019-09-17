#控制台获取整数

# num = int(input('请输入整数：'))
#
# # state = '偶数' if num % 2 == 0 else '奇数'
# #
# # print(state)
#
# if num % 2:
#     print('奇数')
# else:
#     print('偶数')

#控制台输入年份，闰年给day赋值29，否则28
# day = None
year = int(input('请输入年份：'))

# if year % 4 == 0  and  year % 100 != 0 or year % 400 == 0:
#     day = 29
# else:
#     day = 28
# print(day)

#改进版：
# if not year % 4 and  year % 100 or not year % 400:
#     day = 29
# else:
#     day = 28
# print(day)

#条件表达式
day = 29 if year % 4 == 0  and  year % 100 != 0 or year % 400 == 0 else 28

print(day)