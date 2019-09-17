'''
核心数据类型
'''

#1.None
name = 'shibw'
#解除变量与数据的绑定
name = None
print(name)
#使用None占位
stu_name = None

#2.整形 int
#十进制　０～９
num1 = 20
#二进制　０　１
print(0b10)
#八进制　０～７
print(0o10)
#十六进制　０～９　a(10)~f(15)
print(0x10)

#复数
print(1+1J)
print(0+1J)
print(1J)
print(1j)

#数据类型转换
int_dol = int(input('请输入美元：') )

print('转换人民币:' + str(int_dol * 6.9) + '元')


print(bool(' ')) #True 包含空格
print(bool('0')) #True
print(bool(''))  #Flase
print(bool(0))   #Flase
print(bool(0.0)) #Flase
print(bool(None)) #Flase





