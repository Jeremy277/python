#1.在1-100之间给定数字，电脑来猜，直到猜对为止。
import random

y = int(input('电脑要猜的数字（1-100）：'))
i = 1
j = 100
n = 0

if 1 <= y <= 100:
    while True:
        c = random.randint(i,j)  
        if c == y:
            print('电脑猜了%d次，正确数字是%d。' % (n,c))  
            break
        elif c > y:
            print('猜大了', c ,'。')
            j = c
            n += 1
        else:
            print('猜小了', c ,'。')
            i = c
            n +=1
else:
    print('输入数字超范围。')
