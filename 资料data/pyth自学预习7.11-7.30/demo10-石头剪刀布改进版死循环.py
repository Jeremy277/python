import random
menu = '''(0)石头
(1)剪刀
(2)布
(q)退出
请出拳(0/1/2):'''
all_list = ['石头','剪刀','布']
win_list = [['石头','剪刀'],['剪刀','布'],['布','石头']]

while True:
    c = random.choice(all_list)
    y = input(menu)
    if y.strip().lower() in ['0','1','2','q']:
        if y.strip().lower() == 'q':
            print('\033[31m猜拳游戏退出\033[0m')
            break
        elif [all_list[int(y)],c] in win_list:
            print('你出拳：%s 电脑出拳：%s 你赢了' % (all_list[int(y)],c))
        elif all_list[int(y)] == c:
            print('你出拳：%s 电脑出拳：%s 平局' % (all_list[int(y)],c))
        else:
            print('你出拳：%s 电脑出拳：%s 你输了' % (all_list[int(y)],c))
    else:
        print('\033[33m选择无效\33[0m')
