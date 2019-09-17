#随机加法测试
import random

sum_1 = 0
score = 0
count = 0

for i in range(5):
    num_1 = random.randint(1, 20)
    num_2 = random.randint(1, 20)
    sum_1 = num_1 + num_2
    print('请回答:%d+%d=？' % (num_1,num_2))
    user = input('输入正确答案：')
    if user.isdigit():
        user = int(user)
        if user == sum_1:
            score += 20
            count += 1
            print('\33[31m回答正确\33[0m')
        else:
            print('\33[32m回答错误\33[0m')
    else:
        print('\33[34m输入非法\33[0m')

print('\33[31m\n总共5道题，答对%d道，得分%d\33[0m' % (count,score))

