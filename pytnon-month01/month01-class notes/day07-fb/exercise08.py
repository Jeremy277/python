#定义一个两个数字相加的函数

def myadd(num1,num2):
    '''

    :param num1:
    :param num2:
    :return:
    '''
    return num1 + num2

# print(myadd(1,2))

#定义4位整数,每一位相加和:
def sum_wei(num):
    '''
    计算整数每位相加结果
    :param num: 4位整数
    :return: 每一位相加和
    '''
    result = num % 10
    result += num // 10 % 10
    result += num // 100 % 10
    result += num // 1000
    return result

print(sum_wei(1234))
