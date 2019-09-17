#累加从10-50的个位不是3 6 9 的数字

sum_1 = 0
for i in range(10,51):

    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        continue
    sum_1 += i
    print(i,end=' ')
print('\n',sum_1)