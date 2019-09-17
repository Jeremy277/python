# s = '王者荣耀'

# for m in s:
#     print(m,end = ' ')

# n = int(input ('请输入一个整数：'))
# for i in range(2,1+n,2):
#     print(i,end = ' ')

#随机生成20以内加减法的程序
import random

print('''
******************
 小可爱专用 V1.0
    ^_^
******************
开始答题了！
''')
correct = 0
wrong = 0

for i in range(7):

    n1 = random.randint(1,20)
    n2 = random.randint(1,20)
    s = '+-'
    option = random.choice(s)

    if n1 < n2 and option == '-':
        result = int(input('%d %s %d = ' % (n2,option,n1)))
        if result == n2 - n1:
            print('恭喜我的小可爱，你答对啦！继续努力...')
            correct +=1
        else:
            print('好可惜，还差一点点，正确答案是%d' % (n2 - n1))
            wrong +=1
    elif option =='-':
        result = int(input('%d %s %d = ' % (n1,option,n2)))
        if result == n1 - n2:
            print('恭喜我的小可爱，你答对啦！继续努力...')
            correct +=1
        else:
            print('好可惜，还差一点点，正确答案是%d' % (n1 - n2))
            wrong +=1
    else:
        result = int(input('%d %s %d = ' % (n1,option,n2)))
        if result == n1 + n2:
            print('恭喜我的小可爱，你答对啦！继续努力...')
            correct +=1
        else:
            print('好可惜，还差一点点，正确答案是%d' % (n1 + n2))
            wrong +=1

print('总共7道题，我的小可爱答对%d道，错误%d道^_^' % (correct,wrong))




