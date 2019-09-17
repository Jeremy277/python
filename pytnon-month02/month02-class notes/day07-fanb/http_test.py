'''
        http请求响应
'''
from socket import *

#tcp服务端
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',5299))
s.listen(5)

c,addr = s.accept()
print('connect from>>',addr)

data = c.recv(4096)
print('recv>>',data.decode())
#谷歌浏览器响应必须满足http响应格式
html = '''
HTTP/1.1 200 OK
Content-Type: text/html

<h1>Hello World</h1>
'''
c.send(html.encode())

c.close()
s.close()
