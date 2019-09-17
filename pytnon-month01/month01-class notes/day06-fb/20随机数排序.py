import random

list_1 = list(range(100))
list_2 = random.sample(list_1,20)
list_3 = []
# list_2.sort()
print(list_2)
min_value = list_2[0]
for i in range(len(list_2)):
    for j in list_2:
        if j < min_value:
            min_value = j
            list_2.remove(j)
            list_3.append(j)
            print(list_3)

print(list_3)
