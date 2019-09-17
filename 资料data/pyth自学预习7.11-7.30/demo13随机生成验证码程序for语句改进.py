#1.实现随机生成n位验证码（字母 数字 下划线）
import random
import string

all_chars = string.ascii_letters + string.digits + '_'
i = 1
n = int(input('请输入验证码位数：'))
#定义一个空字符串变量
pwd = ''
#控制循环次数
for i in range(n):
    char = random.choice(all_chars)
    pwd = pwd + char
print(pwd)
