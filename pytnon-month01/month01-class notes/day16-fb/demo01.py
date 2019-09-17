import sys
import time

print(sys.path)
sys.path.append('/home/tarena/pytnon-month01'
                '/month01-课堂笔记/day16-fb')
#append上一级路径   才能在终端中运行代码
print(sys.path)
print(sys.argv)#python位置参数列表

# print(time.time())#从计算机元年开始计数1970.1.1
# print(time.localtime(1))
# time_tuole = time.localtime()
# print(time.mktime(time_tuole))
# print(time.strftime('%y/%m/%d %H:%H:%S',time_tuole))
# print(time.strftime('%Y-%m-%d %H:%H:%S',time_tuole))
