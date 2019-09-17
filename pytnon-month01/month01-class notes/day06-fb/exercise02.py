#利用容器判断某月有几天
#


year = int(input('请输入年:'))
month = int(input('请输入月:'))

# if year % 4 ==0 and year % 100 != 0 or\
# year % 400 == 0 and month == 2:
#     print(days[1] + 1)
# else:
#     print(days[month-1])

if month<1 or month >12:
    print('输入错误')
else:
    month02 = 29 if year % 4 ==0 and \
    year % 100 != 0 or year % 400 == 0\
        else 28
    days = (31, month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(days[month - 1])


