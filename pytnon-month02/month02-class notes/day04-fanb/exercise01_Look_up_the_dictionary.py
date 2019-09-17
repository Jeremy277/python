#练习查字典：
#通过单词查找释义
f = open('dict.txt','r')
# dict_dict = {}
#
# while True:
#     data_key = f.read(16)
#     if data_key:
#         data_value = f.readline()
#         data_key1 =data_key.strip()
#         data_value1 = data_value.strip()
#         dict_dict[data_key1] = data_value1
#     else:
#         break
# word = input('输入单词：')
# try:
#     print('单词释义：',dict_dict[word])
# except KeyError:
#     print('查无此项')
# f.close()
#方法2：
word = input("单词:")

# 打开文件
f = open('dict.txt')

for line in f:
    w = line.split(' ')[0]
    # 遍历的单词已经大于目标,说明找不到了
    if w > word:
        print("没有找到该单词")
        break
    elif w == word:
        print(line)
        break
else:
    print("没有找到该单词")

f.close()



