#将英文反转

str_1 = 'How are you'

list_1 = str_1.split(' ')
str_1 = ' '.join(list_1)[::-1]

print(list_1)
print(str_1)