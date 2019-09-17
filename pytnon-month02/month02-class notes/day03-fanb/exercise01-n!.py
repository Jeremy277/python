'''
    n的阶乘
'''

# def factorial(n):
#     reslut = 1
#     for i in range(1,n+1):
#         reslut *= i
#     return reslut

#递归函数
def factorial(n):
    #递归终止条件
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))
