'''
    复制文件夹百分比
'''

import os
from multiprocessing import Pool,Process,Queue

#消息队列
q = Queue(4)
#拷贝文件
def copy_file(file,old_dir,new_dir):
    fr = open(old_dir + file,'rb')
    fw = open(new_dir + file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data)
        #消息队列
        q.put(n)

# 创建进程池
def main():
    path = '/home/tarena/'
    dir = input('请输入要拷贝的文件目录：')
    old_dir = path + dir + '/'
    new_dir = path + dir + '_备份/'
    # os.removedirs(new_dir)
    os.mkdir(new_dir) #再次运行会报错 文件夹已存在
    file_list = os.listdir(old_dir)

    #计算文件大小
    total_size = 0
    for file in file_list:
        total_size += os.path.getsize(old_dir + file)
    print('总共大小：%.2fM'%(total_size/1024/1024))

    #添加进程池
    pool = Pool(4)
    for file in file_list:
        pool.apply_async(func=copy_file,args=(file,old_dir,new_dir))
    pool.close()

    #计算百分比
    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get()
        print('拷贝了%.4f%%'%(copy_size/total_size*100))

    pool.join()


if __name__ == '__main__':
    main()


