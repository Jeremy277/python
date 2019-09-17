'''
函数参数传递
形参'''
#打印矩形
# def fun_1(row,col=3,char = '*'):
#     for r in range(row):
#         for c in range(col):
#             print(char,end=' ')
#         print()
# fun_1(3,4)

#星号元组形参
# def fun_2(p1,p2,*args):
#     print(p1)
#     print(p2)
#     print(*args)
#
# fun_2(1,2,3,4,5,6,7,8,9,10)
# fun_2(1,2)

# def fun_3(*args,sep=' ',end = '\n',file = None):
#
#     print(*args,sep = sep,end = end)
#
# fun_3(1,2,3,4,sep = '/')

# def fun_4(*,p1=0,p2):
#     print(p1)
#     print(p2)
#
# fun_4(p2=1,p1=2)

def fun_5(a,*args,b = 2,c,**kwargs,):
    print(a)
    print(args)
    print(b)
    print(c)
    print(kwargs)


# fun_5(1,c=2)
# fun_5(1,5,6,7,c=2,d=4)

def fun_6(*args,**kwargs):
    print(*args)
    # for i in args:
    #     print(i)
    for k,v in kwargs.items():
        print(k,v)


fun_6(1,2,3,6,5,4,a=1,c=2)