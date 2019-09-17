# s = b'hello'
# print(type(s),'\n',s)
# h = '你好'.encode()
# print(h)
# z = h.decode()
# print(z)

#打开文件
# try:
#     '''
#         文本文件既可以使用文本方式打开，也能使用二进制文件打开
#         二进制文件如果使用文本方式打开，读写会报错
#     '''
    # f = open('text.py','r')#只读
#     # f = open('text.py','w')#只写
#     # f = open('text.py','a')#追加
# except Exception as e:
#     print(e)
f = open('test','r')
#1.读写件
# f = open('ship.bmp','rb')
# while True:
#     data = f.read(16)
#     if data:
#         print(data)
#     else:
#         break
#2.读取一行
data = f.readline(1)
print('读取一行内容',data)
# data = f.readline()
# print('读取一行内容',data)
#3.将内容读取到一个列表
# data = f.readlines()
#4.文件对象可迭代，每次打印一行
# print('读取一行内容',data)
for line in f:
    print(line)
#关闭文件
f.close()
