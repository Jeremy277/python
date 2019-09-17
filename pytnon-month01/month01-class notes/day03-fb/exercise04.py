#在控制台分别输入4个数字，打印最大的数字

num_1 = int(input('请输入第1个数字：'))
num_2 = int(input('请输入第2个数字：'))
num_3 = int(input('请输入第3个数字：'))
num_4 = int(input('请输入第4个数字：'))
#1.输入2个数字
# if num_1 > num_2:
#     print(num_1)
# elif num_1 == num_2:
#     print(num_1)
# else:
#     print(num_2)
#2.输入3个数字
# if num_1 >= num_2:
#     if num_1 >= num_3:
#         print(num_1)
#     else:
#         print(num_3)
# elif num_2 >= num_1:
#     if num_2 >= num_3:
#         print(num_2)
#     else:
#         print(num_3)


#3.输入4个数字
max_value = num_1

if max_value < num_2:
    max_value = num_2
if max_value < num_3:
    max_value = num_3
if max_value < num_4:
    max_value = num_4
    print(max_value)


# if num_1 >= num_2 and num_1 >=num_3 and num_1 >= num_4:
#     print(num_1)
# elif num_2 >= num_1 and num_2 >=num_3 and num_2 >= num_4:
#     print(num_2)
# elif num_3 >= num_1 and num_3 >=num_2 and num_3 >= num_4:
#     print(num_3)
# else:
#     print(num_4)