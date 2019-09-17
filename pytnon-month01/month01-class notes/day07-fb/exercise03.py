#for嵌套
#方法一:
# for j in range(2):
#     print('*' * 5)
#     print('#' * 5)

#方法二:
for i in range(4):
    for j in range(5):
        if i % 2 ==0:
            print('*',end=' ')
        else:
            print('#', end=' ')
    print()

