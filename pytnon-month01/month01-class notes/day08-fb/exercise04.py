#定义函数myprint, 统计该函数调用的次数

count = 0
def myprint():
    global count
    count += 1
    print(count)

myprint()
myprint()
myprint()
myprint()