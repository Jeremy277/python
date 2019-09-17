# name = input('请输入姓名：')
# age = int(input('请输入年龄:'))

# print('您刚输入的姓名是：%s,年龄为%d。'%(name,age))

#1.输入一个人的周岁，将其虚岁给打印出来。
# age = int(input('请输入周岁：'))

# print('其虚岁为:',age+1)
# print('其虚岁为:%d'%(age+1)


#2.输入两个整数a和b，计算这两个数的和、差、成绩、a的b次方。
# number1 = int(input('请输入第一个整数：'))
# number2 = int(input('请输入第二个整数：'))

# print('其和为：',number1+number2)
# print('其差为：',number1-number2)
# print('其乘积为：',number1*number2)
# print('其幂为：',number1**number2)
# print('%d + %d = %d' % (number1,number2,number1 + number2))
# print('%d - %d = %d' % (number1,number2,number1 - number2))
# print('%d * %d = %d' % (number1,number2,number1 * number2))
# print('%d ** %d = %d' % (number1,number2,number1 ** number2))

#3.写一个程序，定义一个合同样式。
# jia = input('甲方姓名：')
# yi = input('乙方姓名：')
# money = int(input('合同金额：'))
# year = int(input('输入年份：'))
# month = int(input('输入月份：'))
# day = int(input('输入日期：'))
# menu = '''
# 甲方:_%s_ 乙方:_%s_
# 合同金额:_%.2f_
# ......
# 日期:_%d_年_%d_月_%d_日
# '''
# print(menu  % (jia,yi,money,year,month,day))

#4.分3次、输入当前的小时，分钟，秒数，打印：从0:0：0到现在一共过了多少秒。
hour = int(input('请当前输入小时:'))
minute = int(input('请当前输入分钟:'))
second = int(input('请当前输入秒数:'))
total = hour*3600+minute*60+second

print('从0:0:0到现在为止已经过了%d秒' % total)