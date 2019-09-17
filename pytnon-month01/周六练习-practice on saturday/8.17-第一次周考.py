# print(bool(None))

# s = 'ABCDEFG'

# print(s[3])
# print(s[-6:5])
# print(s[:6])
# print(s[-1:])
# print(s[::-1])

# print(bool(s[0:-1:-1]))
#
# L =[1,2,3,4,5,6,7]
# L1 = L[::2]
# L2 = L[::-3]
# print(L1)
# print(L2)
#
# print(len("\\\nhello"))
#列表嵌套式:
list1 =[]
for i in range(2):
    list1.append([])
    for j in range(1,4):
        list1[i].append(j+i*3)
print(list1)#[[1, 2, 3], [4, 5, 6]]

#列表嵌套式:
print([[j+i*3 for j in range(1,4)] for i in range(2)])


list01 = [[1+i*3,2+i*3,3+i*3] for i in range(2)]
print(list01)


# L = [1,2,3]
# def fn2(x):
#     x = [4,5,6]
#     print(id(x))
# fn2(L)
# print(L)
# print(id(L))
# for i in range(1,5,2):
# 	print(i)
# 	for j in range(3):
# 		if  j == 2:
# 			break
# 		print(j)
# L = [1,  2,  3,  4,  5]
# L2 = [ str(i)  for  i  in  L  if  i%2==0 ]
# print(L2)
#
# def f1():
#     v = 200
#     def f2():
#         v = 300
#         def f3():
#             nonlocal v
#             v = 400
#         f3()
#         print('f2.v= ',v )
#     f2()
#     print('f1.v=',v)
# f1()
l = [1,2,3,4,5,6]
l1 = []
for c in l:
    l1.append(str(c))
str01 = '|'.join(l1)
print(str01)
print('|'.join(str(c) for c in l))
#
str01 = 'welcome to beijng'
str02 = str01[-11::-1] +str01[10:6:-1] +str01[16:10:-1]
print(str02)#emoclew ot gnjieb
str01 = str01[::-1]#gnjieb ot emoclew
str01 = str01.split()#['gnjieb', 'ot', 'emoclew']
str01 = str01[::-1]#['emoclew', 'ot', 'gnjieb']
str01 = ' '.join(str01)#emoclew ot gnjieb
print(str01)

#
# s= {1,2,3}
# s.add(4)
# print(s)
#
# print(max(['11', '2', '3']))

print('A'>'69785')


#行列转换
game_map = [
    [1,2,3,4,5],
    [5,6,7,8,6],
    [9,10,11,12,7],
    [13,14,15,16,8]]

list_1 = []
#方法一:
for i in range(len(game_map[0])):
    list_1.append([])
    for row in game_map:
        list_1[i].append(row[i])
    # for j in range(len(game_map)):
    #     list_1[i].append(game_map[j][i])
print(list_1)
#方法二:
# for i in range(5):
#     list_1.append([row[i] for row in game_map])
# print(list_1)
#方法三:
print([[row[i] for row in game_map]for i in range(len(game_map[0]))])