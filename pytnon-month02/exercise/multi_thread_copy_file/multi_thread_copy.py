'''
    利用多线程模拟下载器下载资源
'''
import os
from threading import Thread

#1.创建服务器目录
usls = [
    '/home/tarena/桌面/',
    '/home/tarena/模板/',
    '/home/tarena/视频/',
    '/home/tarena/图片/',
    '/home/tarena/文档/',
    '/home/tarena/下载/',
    '/home/tarena/音乐/'
]
#2.在目录中查找存在资源的文件夹
file_exist_list = []
filename = input('请输入需要下载资源：')
for i in usls:
    path = i+filename
    if os.path.exists(path):
        file_exist_list.append(path)

#3.按照存在资源的文件夹划分线程及每一线程需要下载的字节
n = len(file_exist_list)
if n <= 0:
    print()
all_size = os.path.getsize(file_exist_list[0])
part_size = all_size//n + 1

downloda_file = open(filename,'wb')
#4.下载函数
def downloda(path,n):
    f = open(path,'rb')
    seek_size = part_size * n
    f.seek(seek_size)

    while True:
        data = f.read(1024)
        if data:
            pass



#5.创建多线程
objs = []
n = 0
for path in file_exist_list:
    t = Thread(target=downloda,args=(path,n))
    objs.append(t)
    t.start()
    n += 1

for i in objs:
    i.join()






#---------------------------
#测试代码：
print(file_exist_list,n)  #['/home/tarena/视频/风景.png', '/home/tarena/图片/风景.png', '/home/tarena/文档/风景.png'] 3
print(all_size,part_size) #2707021 902341

