'''
    pipe
'''
from multiprocessing import Pipe,Process

#创建管道
fd1,fd2 = Pipe()

def app1():
    print('app1>>启动app1，请登录，（可以使用app2）')
    print('app1>>向app2发请求')
    fd1.send('app1需要：用户名，头像')
    data = fd1.recv()
    print('app1>>ok',data)

def app2():
    data = fd2.recv()
    print('app2>>请求',data)
    fd2.send({'name':'Li','image':'人'})

p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p1.join()