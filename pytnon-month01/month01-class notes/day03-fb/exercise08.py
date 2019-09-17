#在控制台输出 0 1 2 3 4 5
#在控制台输出 2 3 4 5 6 7
#在控制台输出 0 2 4 6 8

num1 = 0
num2 = 2
num3 = 0
num4 = 2
num5 = 1

while num1 <= 5:
    print(num1,end=' ')
    num1 += 1
    if num1 == 6:
        print('\n')
while num2 <= 7:
    print(num2,end=' ')
    num2 += 1
    if num2 == 8:
        print('\n')
while num3 <= 8:
    print(num3,end=' ')
    num3 += 2
    if num3 == 10:
        print('\n')
while num4 <= 20:
    print(num4,end=' ')
    num4 += 2
    if num4 == 22:
        print('\n')
while num5 <= 20:
    num5 += 1
    if not num5 % 2 :
        print(num5,end=' ')



