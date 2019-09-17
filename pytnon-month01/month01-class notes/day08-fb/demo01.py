# def func_1():
#     a = 100
#     print(a)
# #开辟栈帧
# func_1()
# #栈帧销毁
# def func_2(p):
#     p = 100
#
# a01 = 1
# func_2(a01)
# print(a01)

# def func_3(p1,p2):
#     p1,p2 = p2,p1
#     return p1,p2
#
# print(func_3(1,10))
# print(func_3(p2=10,p1=1))

a01 = ['孙悟空']
a02 = ['猪八戒']
# def func_3(p1,p2):
#     p1[0] = '悟空'
#     p2 = '八戒'#修改栈帧中变量的指向
# func_3(a01,a02)
# print(a01)  #['悟空']
# print(a02) #['猪八戒']

# def func_4(p1,p2):
#     p1[:] = ['悟空']#切片赋值 修改源列表
#     temp = p2[:]#浅拷贝 列表和原列表是两个列表
#     temp[:] = ['八戒']
#
# func_4(a01,a02)
# print(a01)#['悟空']
# print(a02)#['猪八戒']

def func_3(p1,p2):
    p1 = '悟空'
    p2[0] = '八戒'

a = 100
b = [200]
func_3(a,b)
print(a)  #100
print(b)#['八戒']