import random
import string

all_letters = string.ascii_letters
right = 0
wrong = 0


for i in range(5):
   
    computer = random.choice(all_letters)
    #computer = random.sample(all_letters,7)

    print ('字符%s' % computer)

    you = input('请输入上述字符：')
    if computer == you:
        print('输入正确，继续....')
        right +=1
    else:
        print('输入错误，继续')
        wrong +=1

print('正确%d个，错误%d个' % (right,wrong))


