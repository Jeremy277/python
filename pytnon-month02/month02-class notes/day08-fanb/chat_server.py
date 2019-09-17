"""
    群聊天服务端
"""
from socket import *
import os,sys

#全局变量
HOST = '0.0.0.0'
PORT = 5277
ADDR = (HOST,PORT)

#存储用户{name:address}
user = {}

#处理用户登录
def do_login(s,name,addr):
    if name in user or '管理员' in name:
        s.sendto('用户名已存在！'.encode(),addr)
    else:
        s.sendto(b'OK',addr)  #可以进入
    #先通知其他人
    msg = '欢迎 %s 加入群聊天' % name
    for others in user:
        s.sendto(msg.encode(),user[others])
    user[name] = addr #加入字典

#处理聊天
def do_chat(s,name,text):
    msg = '%s : %s' % (name,text)
    for others in user:
        #不发送自己
        if others != name:
            s.sendto(msg.encode(),user[others])

#处理退出
def do_quit(s,name):
    msg = '%s 退出了群聊天'%name
    for others in user:
        if others == name:
            s.sendto(b'EXIT',user[others])
        s.sendto(msg.encode(),user[others])
    del user[name]


#循环接受客户端请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)
        tmp = data.decode().split(' ',2)
        #根据不同的请求类型，执行不同的事件
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)
        elif tmp[0] == 'C':
            do_chat(s,tmp[1],tmp[2])
        elif tmp[0] == 'Q':
            do_quit(s,tmp[1])



#搭建网络
def main():
    #udp
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)
    pid = os.fork()
    if pid == 0:
        #管理员消息处理
        while True:
            msg = input('管理员消息：')
            msg = 'C 管理员' + msg
            s.sendto(msg.encode(),ADDR)

    else:
        do_request(s) #接受客户端请求

if __name__ == '__main__':
    main()


