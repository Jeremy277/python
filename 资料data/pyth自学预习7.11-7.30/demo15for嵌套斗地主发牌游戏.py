# 红桃:\033[31m\u2665\033[0m
# 黑桃:\u2660
# 方片:\u2666
# 梅花:\u2663

import random

# #生成54张牌
kinds = ['\u2665','\u2660','\u2666','\u2663']
number = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
kings = ['大王','小王']

for kind in kinds:
    for n in number:
        kings.append(kind + n)
#测试
# print(kings)
# print(len(kings))

#洗牌
random.shuffle(kings)
#切片
p1 = kings[0:17]
p2 = kings[17:34]
p3 = kings[34:51]
card = kings[51:]

print(p1)
print(p2)
print(p3)
print(card)
         


