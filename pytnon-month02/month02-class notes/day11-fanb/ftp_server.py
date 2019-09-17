'''
    ftp 文件服务器
'''
from socket import *
from threading import Thread
import sys,os
from time import sleep

#全局变量
HOST = '0.0.0.0'
PORT = 5277
ADDR = (HOST,PORT)
FTP = '/home/tarena/FTP/'  #文件库位置

files = os.listdir(FTP)
print(files)
#实现具体功能
class FtpServer(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    def do_list(self):
        files = os.listdir(FTP)
        if not files:
            self.connfd.send('充值vip，走向人生巅峰')
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
            filelist = ''
            for file in files:
                if file[0] != '.' and os.path.isfile(FTP + file):
                    filelist += file + '\n'
            self.connfd.send(filelist.encode())
        # for file in files:
        #     #文件类型判断
        #     if file[0]!='.' and os.path.isfile(FTP+file):
        #         sleep(0.1)
        #         self.connfd.send(file.encode())
        # sleep(0.1)
        # self.connfd.send(b'##')

    def do_get(self,filename):
        try:
            f = open(FTP + filename,'rb')
        except Exception:
            self.connfd.send('仅有VIP可以下载'.encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)  #防止ok和文件粘在一起

        while True:
            data = f.read(1024)
            if not data:
                sleep(0.1)  #防止##和ok粘到一起
                self.connfd.send(b'##')
                break
            self.connfd.send(data)


        # file = self.connfd.recv(128).decode()
        # files = os.listdir(FTP)
        # print(files)
        # if file in files:
        #     print('文件存在')
        #     f = open(FTP+file,'rb')
        #     while True:
        #         data = f.read(1024).decode()
        #         if not data:
        #             break
        #         self.connfd.send(data)
        #     f.close()
    def do_put(self,filename):
        if os.path.exists(FTP+filename):
            self.connfd.send('文件已存在'.encode())
            return
        else:
            self.connfd.send(b'OK')
        f = open(FTP+filename,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            f.write(data)
        f.close()


    #分配任务
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            #判断请求类型
            if not data or data == 'Q':
                return #线程结束
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                filename = data.split(' ')[-1]
                self.do_put(filename)

#搭建网络并发模型

def main():
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(ADDR)
    s.listen(5)


    print("Listen the port 5277...")
    while True:
        # 循环等待客户端连接
        try:
            c, addr = s.accept()
            print("Connect from", addr)
        except KeyboardInterrupt as e:
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue

        # 创建线程
        t = FtpServer(c)
        t.setDaemon(True)
        t.start()

if __name__ == '__main__':
    main()