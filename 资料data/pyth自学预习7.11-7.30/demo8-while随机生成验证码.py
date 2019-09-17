#打印整数串
# n = int(input('请输入一个整数:'))
# i = 1

# while i <= n:
#     print(i)
#     i = i + 1

#1.实现随机生成n位验证码（字母 数字 下划线）
import random
import string

all_chars = string.ascii_letters + string.digits + '_'
i = 1
n = int(input('请输入验证码位数：'))
pwd = ''
while i <= n:
    char = random.choice(all_chars)
    pwd = pwd + char
    i = i + 1
print(pwd)

