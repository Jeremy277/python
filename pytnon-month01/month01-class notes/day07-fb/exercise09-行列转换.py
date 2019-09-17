a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]]
b = []

for i in range(len(a[0])):  # 行数
    t = []
    for j in range(len(a)):
        t.append(a[j][i])
    b.append(t)
print(b)

