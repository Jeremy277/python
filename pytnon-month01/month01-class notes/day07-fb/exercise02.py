#交集
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 & s2
print(s3)
#并集
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
print(s3)
#补集
s1 = {1,2,3}
s2 = {2,3,4}
s3 = (s1 - s2)|(s2 - s1)
s4 = s1 ^ s2
print(s3)
print(s4)
#子集 <   超集 >
s1 = {1,2,3}   #超集
s2 = {2,3,}   #子集
print(s1 > s2)
print(s2 < s1)
#相同或不同
s1 = {1,2,3}
s2 = {2,3,4}
print(s1 == s2)
print(s1 != s2)
#lianxi

dic_1 = {'经理':{'曹操','刘备','孙权'},
         '技术':{'曹操','刘备','关羽','张飞'}}

print(dic_1['经理']&dic_1['技术'])
print(dic_1['技术']-dic_1['经理'])

if '张飞' in dic_1['经理']:
    print('张飞是经理')
else:
    print('张飞不是经理')
print('张飞' in dic_1['经理'])
print('共有:%d人' %  len(dic_1['技术'] |dic_1['技术']))

print(dic_1['技术']^dic_1['经理'])

