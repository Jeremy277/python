#输入成绩,若为空退出,获取最高分,最低分,平均分

#定义空列表
list_1 = []
# #循环添加数据到空列表
while True:
    name = input('请输入学生成绩:')
    if name == 'exit':
        print('退出')
        break
    list_1.append(int(name))
# #打印列表中每个元素
print('最高分',max(list_1))
print('最低分',min(list_1))
print('平均分',sum(list_1)/len(list_1))


str1 = '123456'
list_2 = []

for i in str1:
    list_2.append(int(i))
print(list_2)
print(sum(list_2))