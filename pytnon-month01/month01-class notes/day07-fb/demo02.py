#集合推导式
set_1 = set()
# for i in range(10):
#     set_1.add(i)
# print(set_1)

set_1 = {i for i in range(10)}
print(set_1)

set_1 = {i for i in range(10) if i%2}
print(set_1)