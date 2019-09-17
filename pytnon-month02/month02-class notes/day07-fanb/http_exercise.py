'''
        http响应
'''
from socket import *

#客户端交互
def handle(c):
    #获取http请求
    data = c.recv(4096).decode()
    print(data)
    request_line = data.split('\n')[0]
    print(request_line)
    info = request_line.split(' ')[1]
    print(info)
    if info == '/':
        with open('index.html') as f:
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += f.read()
    else:
        response = 'HTTP/1.1 404 Not Found\r\n'
        response += 'Content-Type:text/html\r\n'
        response += '\r\n'
        response += '<h1>Sorry...</h1>'
    c.send(response.encode())

#搭建网络
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 5277))
    s.listen(5)
    while True:
        try:
            c,addr = s.accept()
            print('Connect from',addr)
            #处理客户端请求
            handle(c)
        except KeyboardInterrupt:
            print('exit')

main()






