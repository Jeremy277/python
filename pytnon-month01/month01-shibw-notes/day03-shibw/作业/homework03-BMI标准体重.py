# 3.根据身高和体重 参照BMI 返回身体状况
# BMI 体重(kg)/身高(m)**2
# 中国参考标准
# BMI<18.5   体重过低
# 18.5<=BMI<24   正常
# 24<=BMI<28     超重
# 28<=BMI<30     I度肥胖
# ...

weight = float(input('请输入体重（kg）：'))
height = float(input('请输入身高（m）'))
BMI = weight / height **2
#简化比较逻辑，前述以判断的，无需再判断
if BMI < 18.5:
    print(BMI,'体重过低')
elif BMI < 24:
    print(BMI,'正常')
elif BMI < 28:
    print(BMI,'超重')
elif BMI < 30:
    print(BMI,'1级肥胖')
else:
    print(BMI,'太胖了 没救了')


