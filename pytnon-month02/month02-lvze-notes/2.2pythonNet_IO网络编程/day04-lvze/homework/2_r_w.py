# 以r + 或者w + 方式打开文件, 先写入内容, 然后能否将写入的内容读到
# f = open('homework','w+')
# with open('homework','w+') as f:
#     for i in range(5):
#         f.write(str(i)+'\n')
#     f.seek(0)#定位到文件开头，读文件信息
#     print(f.read())

with open('homework','r+') as f:
    for i in range(6):
        f.write(str(i)+'\n')
    f.seek(0)#seek() 方法用于移动文件读取指针到指定位置。
    print(f.read())
