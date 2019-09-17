'''
    ftp 文件服务 . 客户端
'''
from socket import *
import sys
from time import sleep

# 服务器地址
ADDR = ('127.0.0.1',5277)
#实现具体功能
class FtpClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_quit(self):
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit('谢谢使用！')

    def do_list(self):
        self.sockfd.send(b'L')
        #等待服务器回复，是否存在文件列表
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(1024*1024).decode()
            print(data)

            # while True:
            #     data = self.sockfd.recv(128).decode()
            #     if data == '##':
            #         break
            #     print(data)

        else:
            print(data)  #不可以查看的原因
    def do_get(self,filename):

        self.sockfd.send(('G '+filename).encode())
        data = self.sockfd.recv(128).decode()

        if data == 'OK':
            f = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                f.write(data)
            print('%s下载完成' % filename)
            f.close()
        else:
            print(data)
    def do_put(self,filename):
        try:
            f = open(filename,'rb')
        except Exception:
            print('文件不存在')
            return
        filename = filename.split('/')[-1]
        self.sockfd.send(('P ' + filename).encode())
        #等待回复
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    sleep(0.1)
                    self.sockfd.send(b'##')
                    print('上传完成')
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data.decode())






#网络搭建 和 终端输入命令选项
def main():
    sockfd = socket()  # 默认值
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return
    #实例化对象
    ftp = FtpClient(sockfd)
    #循环发起请求
    while True:
        print('''
===========Command===========
*****        list       ***** 
*****      get file     *****
*****      put file     ***** 
*****        quit       ***** 
=============================''')
        cmd = input('Command:')

        if cmd.strip() == 'quit':
            ftp.do_quit()
        elif cmd.strip() == 'list':
            ftp.do_list()
        elif cmd[:3] == 'get':
            filename = cmd.strip().split()[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.strip().split()[-1]
            ftp.do_put(filename)
        else:
            print('请输入正确命令！')



if __name__ == '__main__':
    main()