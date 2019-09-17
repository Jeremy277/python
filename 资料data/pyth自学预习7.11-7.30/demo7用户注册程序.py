#注册用户程序
# 1.输入用户名（不能包括特殊字符和空白字符）
# 2.输入密码（非明文密码）
import string
import getpass
#定义变量2
all_chars = string.punctuation + string.whitespace
#用户名
username = input('请输入注册用户名：')
#判断用户名
for  u in username:
    if u in all_chars:
        print('用户名不合法')
        #终止循环7
        break

pwd = getpass.getpass('请输入密码：')
print('用户名：%s,密码：%s。'% (username,pwd))

