# name="jer"
# score=33
# # print(name,'的颜值是',score,'分')
# print('%s的颜值是%d'%(name,score))
computer = '石头'
you = '剪刀'

# print('''
# 电脑出拳：%s，
# 你出拳：%s，
# 你输了！
# '''%(computer,you))

# 1.苹果一斤9元，你有100元，能买几斤苹果，还剩多少钱。
number = 100//9
money = 100%9

print('1.能买%d斤苹果，剩余%d元钱。'%(number,money))
#2.假如你现在25周岁，每年365天，计算你过了多少个星期。
week = 25*365//7

print('2.我已经过了%d个星期。'%week)

#3.毕业薪资为10000元，每年涨20%，十年之后你的薪资为多少元。
salary=10000*1.2**10

print('3.十年后你的薪资为%.2f元'%(salary))
#4.一个圆的半径为3cm，计算周长和面积。
circumference = 2*3.14*0.03
area = 3.14*0.03*0.03

print('4.圆的周长为%.4f米，面积为%.4f平方米。'%(circumference,area))
#5.从凌晨00:00，到现在过了65520秒，现在是几点几分几秒。
hour = 65520//3600
minute = 65520%3600//60
second = 65520%60

print('5.现在是%d点%d分%d秒。'%(hour,minute,second))

 