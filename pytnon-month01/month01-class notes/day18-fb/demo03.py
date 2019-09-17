'''
外部嵌套作用域
'''
def f1():
    v = 200
    def f2():
        v = 300
        def f3():
            nonlocal v#在内层函数修改外层嵌套函数内的变量
            v = 400
        f3()
        print('f2.v= ',v )
    f2()
    print('f1.v=',v)
f1()