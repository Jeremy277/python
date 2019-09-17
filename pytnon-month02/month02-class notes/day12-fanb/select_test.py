#IO多路复用
import select
from socket import *

s = socket()
s.bind(('0.0.0.0',5299))
s.listen(3)

print('监控IO')
rs,ws,xs = select.select([s],[],[],5)
print(rs)
print(ws)
print(xs)