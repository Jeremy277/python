#jihecaozuo

#KONGJIHE
set_1 = set()
print(set_1)

set_1 = {'a','b'}
print(set_1)
#不包含重复字符
set_1 = set('abcabc')
print(set_1)

#添加;add添加一个元素
set_1.add('love')
print(set_1)
set_1.add('hate')
print(set_1)

# set_1.add([0,1,2])报错
# #可变类型不能放入集合(不可变类型有数字 字符串 元组)

#删除
set_1.remove('a')
print(set_1)
set_1.discard('5')#若删除的元素不存在不会报错
set_1.discard('b')#若删除的元素不存在不会报错
print(set_1)
#若删除的元素不存在报错
# set_1.remove('x')

#获取所有值

for i in set_1:
    print(i)


