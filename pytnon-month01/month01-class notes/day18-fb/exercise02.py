'''
    装饰器
'''
#添加函数验证权限功能
"""
    使用装饰器,为下列功能添加验证权限的功能.
"""

def print_func_name(func):
    # *args 原函数参数可以无限制
    def wrapper(*args,**kwargs):
        password = input('请输入管理员密码：')# 打印函数名称
        # return 原函数返回值
        if password == 'tarena':
            print('验证权限成功')
            return func(*args,**kwargs)# 调用函数
    return wrapper

@print_func_name
def enter_background():
    print("进入后台")

@print_func_name
def delete_order():
    print("删除订单")

# enter_background()
# delete_order()

import getpass

user_name = input('username:')
password = getpass.getpass('password:')
if user_name == 'you' and password == '123456':
    print('成功')
else:
    print('失败')