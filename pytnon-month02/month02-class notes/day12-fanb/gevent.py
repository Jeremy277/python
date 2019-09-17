'''
    协程函数
'''
# import gevent
#
import gevent


def foo(a,b):
    print('233',a,b)
    print('^_^')

# foo(1,2)
f = gevent.spawn(foo,1,2)
gevent.joinall([f])