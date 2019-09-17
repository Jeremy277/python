#石头剪刀布，复杂版
import random
menu = '''
(0)石头
(1)剪刀
(2)布
请出拳(0/1/2):
'''
you = input(menu)
L = [0,1,2]
c = random.choice(L)


if you == 0 and c == 1 or you == 1 and c == 2 or you == 2 and c == 0:
     print('你赢了。你的出拳为%s,电脑出拳为%s' % (you,c))
elif you == c: 
        print('平局。你的出拳为%s,电脑出拳为%s' % (you,c))
else:
        print('你输了。你的出拳为%s,电脑出拳为%s' % (you,c))
