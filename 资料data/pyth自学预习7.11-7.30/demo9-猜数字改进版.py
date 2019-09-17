#1.计算机在1-100之间随机取数，你来猜，直到猜对位置。
import random 

c = random.randint(1,100)
print(c)
while True:
    y = int(input('请猜数字：'))
    if c == y:
        print('\033[31m恭喜，猜对了\033[0m')#输出文本颜色更改
        break
    elif y > c:
        print('\033[31m猜大了\033[0m')
    else:
        print('\033[31m猜小了\033[0m')
