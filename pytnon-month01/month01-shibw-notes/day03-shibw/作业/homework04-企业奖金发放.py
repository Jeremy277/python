# 4.题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

profit = float(input('请输入企业利润（万元）：'))

if 0 <= profit <= 10:
    bonus = profit * 0.1
    print('员工奖金为%.2f万元' % bonus)
elif 10 <= profit <= 20:
    bonus = 1 + (profit - 10) * 0.075
    print('员工奖金为%.2f万元' % bonus)
elif 20 <= profit <= 40:
    bonus = 1 + 0.75 + (profit - 20) * 0.05
    print('员工奖金为%.2f万元' % bonus)
elif 40 <= profit <= 60:
    bonus = 1.75 + 1 + (profit - 40) * 0.03
    print('员工奖金为%.2f万元' % bonus)
elif 60 <= profit <= 100:
    bonus = 2.75 + 0.6 + (profit - 60) * 0.015
    print('员工奖金为%.2f万元' % bonus)
else:
    bonus = 3.35 + 0.6 + (profit - 100) * 0.01
    print('员工奖金为%.2f万元' % bonus)
#方法二：
# 1.企业奖金发放
i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print ((i-arr[idx])*rat[idx])
        i=arr[idx]
print (r)