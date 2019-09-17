"""
    装饰器
    练习:exercise04-装饰器.py
"""
# def print_func_name(func):
#     def wrapper():
#         print(func.__name__)# 打印函数名称
#         func()# 调用函数
#     return wrapper

# @print_func_name   #相当于say_hello = print_func_name(say_hello)
def say_hello():
    print("hello")

# 拦截:新功能 + 旧功能
# say_hello = print_func_name(say_hello)
#
# def say_goodbye():
#     print("goodbye")
#
# say_hello()
#>>wrapper
# say_hello
# hello

# say_goodbye()

# 需求:在不改变原函数以及调用情况下,增加新功能(打印函数名称).

def print_func_name(func):
    # *args 原函数参数可以无限制
    def wrapper(*args,**kwargs):
        print(func.__name__)# 打印函数名称
        # return 原函数返回值
        return func(*args,**kwargs)# 调用函数
        # #此处语法return func(),若函数有返回值可以直接打印，若没有也不影响，直接调用函数
        # func(*args,**kwargs)# 调用函数   #若func函数没有返回值此处直接调用函数
    return wrapper  #若没有报错TypeError: 'NoneType' object is not callable

@print_func_name
def say_hello():
    print("hello")
    return 1

@print_func_name
def say_goodbye(name):
    print(name,"---goodbye")
    return 2

# print(say_hello())#1
a = say_hello()
print(a)
# print(say_goodbye("qtx"))#2
