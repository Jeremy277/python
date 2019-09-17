# 5.输入某年某月某日，判断这一天是这一年的第几天？
#方法一
# year = int(input('请输入年：'))
# month = int(input('请输入月:'))
# day = int(input('请输入日：'))
# # today = 0
#
# months = [0,31,59,90,120,151,181,212,243,273,304,334]
#
# if 0 < month <= 12:
#     today = months[month-1]
# else:
#     print('输入错误')
#
# today += day
#
# if  (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month > 2:
#     today += 1
#     print('%d年%d月%d日是这一年的第%d天' % (year, month, day, today))
# else:
#     print('%d年%d月%d日是这一年的第%d天' % (year, month, day, today))

#方法二：
year = int(input('请输入年：'))
month = int(input('请输入月:'))
day = int(input('请输入日：'))
sum_day = 0
i = 1
while i < month:
    if i in [1,3,5,7,8,10]:
        sum_day += 31
    elif i in [4,6,9,11]:
        sum_day += 30
    else:
        sum_day += 28
    i += 1

sum_day += day

if  (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month > 2:
    sum_day += 1
    print('%d年%d月%d日是这一年的第%d天' % (year, month, day, sum_day))
else:
    print('%d年%d月%d日是这一年的第%d天' % (year, month, day, sum_day))







