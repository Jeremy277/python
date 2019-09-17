list_1 = ['水','金','地','火','木','土','天王','海王']

print('离太阳最近的行星是:',list_1[0])
print('离太阳最远的行星是:',list_1[-1])
print('太阳和地球之间的行星是:',list_1[:2])
print(list_1)
for i in list_1:
    print('八大行星是:',i)

# list_1.reverse()
# print(list_1)
# for i in list_1:
#     print('倒序八大行星是:',i)
for item in range(len(list_1)-1,-1,-1):
    print(list_1[item])
