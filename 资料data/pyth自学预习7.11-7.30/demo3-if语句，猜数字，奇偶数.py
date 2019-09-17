#1. n判断正负数。以缩进作为语句优先级判断。
# number = int(input('请输入一个数字'))

# if number > 0:
#     print('%d是正数' % number)
# elif number < 0:
#     print('%d是负数' % number)
# else:
#     print('零')

# print('你是最胖的！')


#2.判断奇数偶数。
# number = input('请输入一个数字')
# #转成整型
# number = int(number)

# if number % 2 == 0:
#     print('%d是偶数' % number)
# elif number % 2 != 0:
#     print('%d是奇数' % number)

#3.石头剪刀布
# menu = '''
# (0) = 石头
# (1) = 剪刀
# (2) = 布
# (q) = 退出
# 请出拳(0/1/2/q):'''
# number = input(menu)

# if number == '0':
#     print('你的出拳为：石头')
# elif number == '1':
#     print('你的出拳为：剪刀')
# elif number == '2':
#     print('你的出拳为：布')
# elif number == 'q':
#     print('游戏退出！')
# else:
#     print('请输入0/1/2/q：')

#4.判断年龄是否合法。
# age = int(input('请输入年龄：'))

# if age < 0 or age > 150:
#     print('输入不合法')
# else:
#     print('年龄为%d' % age)

#5.猜数字游戏。
# import random

# computer = random.randint(1,5)
# you = int(input('我想好了，你来猜吧：'))

# if you > computer:
#     print('很遗憾，你猜的数字大了。我选的数字是：',computer)
# elif you < computer:
#     print('和遗憾，你猜的数字小了。我选的数字是：',computer)
# else:
#     print('恭喜你，你猜对了！我选的数字是：',computer)


    

    