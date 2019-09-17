#计算时间的装饰器
import time

def timeit(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print('%s函数执行时长：%.6f'%(func.__name__,end-start))
        return res
    return wrapper