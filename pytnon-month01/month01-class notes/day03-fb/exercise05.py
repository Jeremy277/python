#在控制台输入月份 打印对应天数

month = int(input('请输入月份（1-12）：'))

if month < 1 or month > 12:
    print('输入有误')
elif month == 2:
        print('28')
elif month == 4 or month == 6 or month == 9 or month == 11:
        print('30')
else:
    print('31')

