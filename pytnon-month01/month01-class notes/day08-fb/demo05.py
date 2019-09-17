# g01 = '悟空'
# g02 = '八戒'
# def fun_1():
#     num1 = 100
#     print(num1)
#
#     g02 = '老朱'#先定义了局部变量,在再声明全局变量,
#     print(g02) # 有歧义,Python3.6 版本后报错
#
#     global g03
#     g03 = '老沙'
#
#     global g02
#     g02 = '猪八戒'
#     print(g02)
#
# fun_1()
# print(g03)

# def fun_1():
#     a = 10
#     def fun_2():
#         nonlocal a
#         a += 1
#         print(a)
#     fun_2()
#     print(a)
# fun_1()

def user_info():
    user_name = 'zhangsan'
    user_age = 18
    user_email = 'zhangsan@gov.com'
    gender = '男'
    address = '中南海'
#     return user_name,user_age,\
#            user_email,gender,address
#     return {'username':user_name,'userage':user_age,
#             'useremail':user_email,'gender':gender,
#             'adress':address
#             }
    return locals()  #收集当前的局部变量,保存到字典
#
# print(user_info())
infos = user_info()
# for k,v in infos.items():
#     print(k,v)
# #输出详细信息
print('姓名:%s,年龄:%d,邮箱:%s,'
      '性别:%s,地址:%s.'%
      (infos['user_name'],infos['user_age'],
       infos['user_email'],infos['gender'],
       infos['address'],))