# name = input(':')
# age = int(input(':'))
#
# print("我的名字是%s,年龄是%s" % (name, age))
# print("我的名字是%s,年龄是%d" % (name, age))
# print("我的名字是%s,年龄是%f" % (name, age))

#1.
str_1 = input('请输入字符串:')

print('第一个字符是',str_1[0])
print('倒数第二个字符是',str_1[-2])
print('前两个字符是',str_1[:2])
print('倒序字符串:',str_1[::-1])
print('索引为奇数的字符:',str_1[1::2])
#求字符串长度逻辑:
# count = 0
# for i in str_1:
#     count += 1
#     print(count)
length = len(str_1)
if length % 2:
    # num = length // 2
    num = (length - 1) / 2
    print('中间字符:',str_1[num])
