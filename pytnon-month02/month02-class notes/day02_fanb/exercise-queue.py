from lstack import *
from sstack import *
from squeue import  *


sq = SQueue()
ls = LStack()
ss = SStack()
for i in range(15):
    sq.enqueue(i)

# #出队入栈
# while not sq.is_emty():
#     ls.push(sq.dequeue())
#
# #出栈入队
# while not ls.is_empty():
#     sq.enqueue(ls.pop())

#出队入栈
while not sq.is_emty():
    ss.push(sq.dequeue())

#出栈入队
while not ss.is_empty():
    sq.enqueue(ss.pop())

#---------
while not sq.is_emty():
    print(sq.dequeue())