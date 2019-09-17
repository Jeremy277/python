#lianxi 查字典

f = open('dict.txt')
word = input('输入单词：')
for line in f:
    w = line.split(' ')[0]
    if w > word:
        print('查无此项')
        break
    elif w == word:
        print(line)
        break
else:
    print('查无此项')

f.close()