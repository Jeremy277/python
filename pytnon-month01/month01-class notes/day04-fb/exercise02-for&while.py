#1.打印0123数字，累加0123，累加3579
sum_1 = 0
sum_2 = 0
for i in range(4):
    print(i,end=' ')
    sum_1 += i

print('累加：',sum_1)

for i in range(3,10,2):
    print(i,end=' ')
    sum_2 += i

print('累加：',sum_2)

for i in range(4,-1,-1):
    print(i,end=' ')

#2.假设每张纸0.0001米，折纸10次 求厚度
thick_1 = 0.0001
thick_2 = 0.0001

for i in range(10):
    thick_1 *= 2
print('\n对折10次后为%f米' % thick_1)

#3.折纸多少次为8848米
count = 0

while thick_2 < 8848:
    count += 1
    thick_2 *= 2
print('\n达到8848米需要对折%d次' % count)


