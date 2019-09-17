#获取用户输入的年份和月份、和日期
#计算这是一天的第几天

year = int(input('请输入年:'))
month = int(input('请输入月:'))
day = int(input('请输入日:'))

if month<1 or month >12:
    print('输入错误')
else:
    month02 = 29 if year % 4 ==0 and \
    year % 100 != 0 or year % 400 == 0\
        else 28
    days = (31, month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(days[month - 1])
#方法一:
# for i in range(month-1):
#     total_days += days[i]
total_days = sum(days[:month-1])
total_days +=  day
print(total_days)

