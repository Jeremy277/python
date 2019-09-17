#在控制台录入四位整数
#计算每一位相加的结果
# 显示结果
#方法一
num = int(input('请输入四位整数：'))

# a = num % 10               #个
# b = num // 10 % 10         #十
# c = num // 100 % 10        #百
# d = num // 1000            #千
#
# result = a + b + c + d
#
# print('每一位相加结果为：',result)

#方法二

result = num % 10
result += num // 10 % 10
result += num // 100 % 10
result += num // 1000

print('每一位相加结果为：',result)

#作业：画出方法一 方法二的内存图