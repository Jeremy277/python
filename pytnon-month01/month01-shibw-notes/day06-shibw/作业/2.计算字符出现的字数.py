# 2.计算一个字符串中的字符以及字符出现的次数
# 输入 this is a test string
# t:4 h:1 i:3 s:4 a:1 e:1 r:1 n:1 g:1
#思路
#判断字符出现的次数
#如果统计过 次数加1 如果没统计过则等于1
#setdefult()

# import  string
# print(string.punctuation)
# print(string.ascii_letters)
# print(dir(string))

dic_1 = {}
str_1 = 'this ic a test string'
#方法一:
for ch in str_1:
    if ch not in dic_1:
        dic_1[ch] = 1
    else:
        dic_1[ch] += 1

print(dic_1)

#方法二:
for ch in str_1:
    dic_1.setdefault(ch,0)
    dic_1[ch] += 1

print(dic_1)





