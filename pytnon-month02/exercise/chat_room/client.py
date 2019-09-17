#聊天室-客户端

from socket import *
#定义全局变量
import os,sys

ADDR = ('127.0.0.1',5299)

#1.搭建网络
def main():
    s = socket(AF_INET,SOCK_DGRAM)
    #发送请求 注册昵称
    while True:
        name = input('请输入昵称：')
        msg = 'L ' + name
        s.sendto(msg.encode(),ADDR)
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print('您已经入聊天室！')
            break
        else:
            print(data.decode())
        # # 已经进入聊天室
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(s,name)
    else:
        recv_msg(s)

def send_msg(s,name):
    while True:
        try:
            text = input(">>")
        except KeyboardInterrupt:
            text = 'quit'
        if text.strip() == 'quit':
            msg = "Q " + name
            s.sendto(msg.encode(),ADDR)
            sys.exit("退出聊天室")
        msg = "C %s %s"%(name,text)
        s.sendto(msg.encode(),ADDR)

# 接收消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(4096)
        # 收到exit接收进程结束
        if data.decode() == 'EXIT':
            sys.exit()
        print(data.decode()+'\n>>',end='')
if __name__ == '__main__':
    main()
