#判断输入是否为+ - * / 运算符

num_1 = int(input('请输入第一个数字：'))
op = input('请输入运算符：')
num_2 = int(input('请输入第二个数字'))

if op == '+':
    result = num_1 + num_2
    print(num_1,op,num_2,'=',result)
elif op == '-':
    result = num_1 - num_2
    print(num_1,op,num_2,'=',result)
elif op == '*':
    result = num_1 * num_2
    print(num_1,op,num_2,'=',result)
elif op == '/':
    result = num_1 / num_2
    print(num_1,op,num_2,'=',result)
else:
    print('输入运算符有误！')