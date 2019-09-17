# 4. 创建打印函数运行时间的装饰器
#     def fun01():
#         ...
#
#     fun01()

import time
# def total_time():
#     result = 0
#     start = time.time()#返回运算前时间戳
#     for i in range(100000000):
#         result += i
#     end = time.time()#返回运算后时间戳
#     print(result)
#     print(end - start)
# total_time()

def verif_permissions(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print("函数运行时间：")
        re = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return re



    return wrapper

@verif_permissions
def enter_background():
    res = 0
    for i in range(100000000):
        res += i
    print('进入后台')

@verif_permissions
def delete_order():
    res = 0
    for i in range(100000000):
        res += i
    print('删除订单')


enter_background()
delete_order()
