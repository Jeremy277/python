#打印任务信息:

#数据结构:
#{
# 'dsf':[18,'age',80.0]
#          .....
#}

dic_1 = {}
list_1 = []
while True:
    name= input('输入姓名:')
    if name == '':
        print('退出')
        break

    age = int(input('输入年龄:'))
    sex= input('输入性别:')
    weight = float(input('输入体重:'))

    dic_1[name] = [age,sex,weight]

print(dic_1)

for key,value in dic_1.items():
    print('%s的年龄是%d,性别是%s,体重是%.1f' %
          (key,value[0],value[1],value[2]))


