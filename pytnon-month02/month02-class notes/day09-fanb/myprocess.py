from multiprocessing import Process
import time

# def timeit(f):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         res = f(*args,**kwargs)
#         end_time = time.time()
#         print('%s函数执行时间：%.6f'%(f.__nmae__))




def prime_number():
    for i in range(2,11):
        for j in range(2,i):
            if  i%j==0:
                break
        else:
            print(i)




prime_number()

class Prime(Process):
    def __init__(self,prime,begin,end):
        super().__init__()
        self.prime = prime
        self.begin = begin
        self.end = end













# def verif_permissions(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         print("函数运行时间：")
#         re = func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#         return re
#     return wrapper
#
# @verif_permissions
# def enter_background():
#     res = 0
#     for i in range(100000000):
#         res += i
#     print('进入后台')
#
# @verif_permissions
# def delete_order():
#     res = 0
#     for i in range(100000000):
#         res += i
#     print('删除订单')