#输入学生姓名.保存列表,空字符退出,打印所有姓名
#定义空列表
list_1 = []
#循环添加数据到空列表
while True:
    name = input('请输入学生姓名:')
    if name == '':
        print('退出')
        break
    list_1.append(name)
#打印列表中每个元素
for i in list_1:
    print(i)