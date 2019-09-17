jer = ['长剑','铠甲','盾牌']
# honey = jer
# gege = jer

# print(jer)
# print(honey)
# print(gege)

# honey[1] = '披风'

# print(jer)
# print(honey)
# print(gege)
#切片是副本，与本体不是同一个地址
honey = jer[:]
print(honey)
honey[1] = '披风'

print(honey)
print(jer)


