#面试题:能参与for循环的对象,必须具备什么条件
# --->对象必须具有__iter__()方法
list_01 = [10,2,0,30,4,2]
item = list_01.__iter__()
while True:#StopIteration
    try:
        print(item.__next__())
    except StopIteration:
        print('错误')
        break
#使用元组打印元组中的元素
tuple01 = (4,5,3,6,9,8)

for item in tuple01:
    print(item,end=' ')
#不适用for循环打印字典
dict01= {'张翠山':101,'殷素素':102,'张无忌':103}
item = dict01.__iter__()
while True:#StopIteration
    try:
        key = item.__next__()
        print(key,dict01[key],end=' ')
    except StopIteration:
        break
