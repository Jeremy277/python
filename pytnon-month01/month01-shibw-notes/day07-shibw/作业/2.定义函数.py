# 改代码 将之前写过的练习改成函数
# 如：BMI计算 汇率转换等

#1.BMI


def print_BMI(weight,height):
    # weight = float(input('请输入体重（kg）：'))
    # height = float(input('请输入身高（m）'))
    BMI = round(weight / height **2,2)
    #简化比较逻辑，前述以判断的，无需再判断
    if BMI < 18.5:
        print('体重过低')
    elif BMI < 24:
        print('正常')
    elif BMI < 28:
        print('超重')
    elif BMI < 30:
        print('1级肥胖')
    else:
        print('太胖了 没救了')
    return BMI

print(print_BMI(56,1.6))
print(print_BMI(80,1.6))

#2.汇率转换

def exchange_rate(dollar):
    rmb = dollar * 6.9
    return rmb

print('%d美元可以兑换%.2f人民币.' % (50,exchange_rate(50)))