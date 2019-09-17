#石头剪刀布,复杂版。
# import random
# menu = '''
# (0)石头
# (1)剪刀
# (2)布
# 请出拳(0/1/2):
# '''
# y = input(menu)
# all_list = ['石头','剪刀','布']
# c = random.choice(all_list)
# you = all_list[int(y)]

# if you == c:
#     print('你的出拳：%s，电脑出拳：%s，平局' % (you,c))
# elif (you == '石头' and c == '剪刀') or (you == '剪刀' and c == '布') or (you == '布' and c == '石头'):
#     print('你的出拳：%s，电脑出拳：%s，你赢了' % (you,c))
# else:
#     print('你的出拳：%s，电脑出拳：%s，你输了' % (you,c))    


#简化版
import random
menu = '''
(0)石头
(1)剪刀
(2)布
请出拳(0/1/2):
'''
y = input(menu)
all_list = ['石头','剪刀','布']
c = random.choice(all_list)
you = all_list[int(y)]
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]

if [you,c] in win_list:
    print('你出拳：%s 电脑出拳：%s 你赢了' % (you,c))
elif you == c:
    print('你出拳：%s 电脑出拳：%s 平局' % (you,c))
else:
    print('你出拳：%s 电脑出拳：%s 你输了' % (you,c))
