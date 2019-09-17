#Hero's Inventory

#创建一个有内容的元组
inventory = ('长剑',
    '铠甲',
    '盾牌',
    '治愈药水')

print('\n你的物品:')
#for
for item in inventory:
    print(item)

input('\n按下回车键继续。')
#len
print('你拥有%d件物品。' % len(inventory))

input('\n按下回车键继续。')

#if
if '治愈药水' in inventory:
    print('你还能再活一天。')
#索引
index = int(input('\n 输入仓库里的物品编号：'))
print(index,'号物品是',inventory[index])

#切片
start = int(input('\n输入切片起始点：'))
finish = int(input('\n输入切片终止点：'))

print('仓库[',start,':',finish,']是',end = ' ')
print(inventory[start:finish])
input('\n按下回车键继续。')
#元组连接
chest = ('金子','宝石')
print('你找到了箱子，里面有：')
print(chest)
print('将箱子里的物品放入仓库')

input('\n按下回车键继续。')

inventory += chest
print('你的仓库已更新')
print(inventory)