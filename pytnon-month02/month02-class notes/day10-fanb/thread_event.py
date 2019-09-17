'''
    线程互斥
'''

from threading import Event,Thread

s = None
e = Event()
def 杨子荣():
    print('杨子荣前来拜山头！')
    global s
    s = '天王盖地虎'
    e.set()

t = Thread(target=杨子荣)
t.start()
print('说口令')
e.wait()
if s == '天王盖地虎':
    print('宝塔镇河妖')
    print('兄弟，你来了')
else:
    print('错了，毙了他')

t.join()