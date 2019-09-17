
# #6.计算标准体重。
# menu = '''
# ********************
# 标准体重计算程序 V1.0
#     作者 ：JEREMY

#       1.男性
#       2.女性
# ********************
# 请选择(1/2):'''
# sex = int(input(menu))

# if sex == 1: 
#     height = float(input('请输入男性身高：'))
#     weight = (height - 80) * 0.7
#     print('该男性标准体重为%.2fkg。' % weight)
# elif sex == 2:
#     height = float(input('请输入女性身高：'))
#     weight = (height - 70) * 0.6
#     print('该女性标准体重为%.2fkg。' % weight)
# else:
#     print('输入不规范，请重新输入。')


#6.简化计算标准体重程序。
# menu = '''
# ********************
# 标准体重计算程序 V1.0
#     作者 ：JEREMY

#       1.男性
#       2.女性
# ********************
# 请选择(1/2):'''
# sex = int(input(menu))
# height = float(input('请输入身高：'))

# if height == 1:
#     weight = (height - 80) * 0.7
# elif height == 2:
#     weight = (height - 70) * 0.6
# print('标准体重为%.2fkg。' % weight)

#作业
# 1.任意输入1个字符，判断字符(数字、字母、下划线)是否合法：
# s = input('请输入一个字符：')
# all_chars = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM_'

# if len(s) !=1:
#     print('请输入1个字符！')
# elif s in all_chars:
#     print('您输入的字符为%s。' % s)
# else:
#     print('您输入的字符不合法！')

#2.用程序判断输入的数字是否为合法手机号码.
#在13000000000到18999999999
# phone_num = input('请输入手机号码：')

# if phone_num.isdigit():
#     phone_num = int(phone_num)
#     if 13000000000 < phone_num < 18999999999:
#         print('您输入的手机号为%d。' % phone_num)
#     else:
#         print('手机号超范围！')
# else:
#     print('手机号码必须为数字。')

#3.输入年份，判断是否为闰年。
# year = input('请输入年份：')

# if year.isdigit():
#     year = int(year)
#     if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
#         print('%d是闰年。' % year)
#     else:
#         print('%d是平年。' % year)
# else:
#     print('请输入正确的年份。')

#4.用字符串*打印三角形,要求从终端输入一个整数，代表三角形距离左侧的距离
# 请输入一个整数：10.（相加 相乘）
 
n= input('请输入一个正整数:')

if n.isdigit():
    n = int(n)
    spaces = ' ' * n
    print(spaces + '   *')
    print(spaces + '  ***')
    print(spaces + ' ******')
    print(spaces + '********')
else:
    print('输入非法。')




