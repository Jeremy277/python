#Hero's Inventory
# 创建空元组
inventory = ()
#把元组当条件使用
if not inventory:
    print('You are empty_handed')

input('\nPress the enter key to continue.')
#创建一个有内容的元组
inventory = ('sword',
    'armor',
    'shield',
    'healing potion')
#打印元组
print('\n Tuple inventory is:')
print(inventory)
#打印元组中的各个元素
print('\nYou items:')

for item in inventory:
    print(item)

input('\nPress the enter key to exit.')
