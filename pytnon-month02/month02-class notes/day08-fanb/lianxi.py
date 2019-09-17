# import sys
#
# print('1')
#
# sys.exit('退出')
#
# print('2')
"""
file_read.py
文件读取演示
"""

# 打开文件
f = open('test.txt','r')

# 1.读操作
#
# while True:
#     # 到文件结尾时会读出空字串
#     data = f.read(2)
#     # 到文件结尾跳出循环
#     if not data:
#         break
#     print("读取到的数据:",data)

# 2.每次读取一行内容
data = f.readline(7)
print("一行内容:",data)
data = f.readline()
print("一行内容:",data)

# 3.将内容读取到一个列表
# 参数表达的是读取到该字符数所在的行
# data = f.readlines()
# print(data)

# 4.文件对象可迭代,每次一行
# for line in f:
#     print(line)


# 关闭
f.close()
