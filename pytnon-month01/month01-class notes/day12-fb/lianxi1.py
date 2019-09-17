# str_1 = '^-^'.join(['1','2','3'])
# print(str_1)
#
# list_1 = str_1.split('^-^')
# print(list_1)

# 获取列表的第二个元素
# def takeSecond(elem):
#     return elem[1]
#
#
# # 列表
# random = [(2, 2), (3, 4), (4, 1), (1, 3)]
#
# # 指定第二个元素排序
# random.sort(key=takeSecond)
#
# # 输出类别
# print('排序列表：', random)



# def takeSecond(e

# 列表
random = [
('降龙十八掌',5,9,80),
('九阴白骨爪',4,7,50),
('一阳指',5,2,60),
('打狗棒法',2,10,0)
]

# 指定第二个元素排序
random.sort(key=lambda x: x[2])

# 输出类别
print('排序列表：', random)