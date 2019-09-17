def fun_1(a,b,c):
    print(a,end=' ')
    print(b,end=' ')
    print(c,end=' ')
#
# fun_1(1,2,3)
# fun_1(3,2,1)
#
# list_1 = [1,2,3]
# fun_1(*list_1)
# str_1 = 'abc'
# fun_1(*str_1)
#
# fun_1(c=30,b=20,a=10)

dic_1={'a':10,'b':20,'c':30}
#a = 10,b = 20,c = 30
fun_1(**dic_1)
