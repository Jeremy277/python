#判断是否为素数：被1和自身整除的数

# num = int(input('请输入一个整数：'))
#
# for i in range(2,num):
#     if num % i ==0:
#         print(str(num) + '不是素数')
#         break
# else:
#     print(str(num) + '是素数')



#
for i in range(1,21):
    if i % 2 == 0:
        continue
    print(i,end=' ')

