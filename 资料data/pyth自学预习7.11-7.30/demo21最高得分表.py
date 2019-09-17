# inventory = ['长剑',
#     '铠甲',
#     '盾牌',
#     '治愈药水']

# print(inventory)

# inventory[0] = 'sword'

# print('\n',inventory)

# inventory[4:6] = ['飞镖', '弩箭','匕首', '弩箭','匕首']
# print('\n',inventory)
# del inventory[4:]
# print('\n',inventory)

scores = []
choice = None

while choice != '0':
    print('''
    最高得分表
    
    0 - 退出
    1 - 得分表
    2 - 添加得分
    3 - 删除得分
    4 - 得分乱序''')

    choice = input('请选择：')

    if choice == '0':
        print('再见')
    elif choice == '1':
        print('最高得分表')
        for score in scores:
            print(score)
    elif choice == '2':
        score = int(input('请输入得分：'))
        scores.append(score)
    elif choice == '3':
        score = int(input('请输入需要删除的分数：'))
        if score in scores:
            scores.remove(score)
        else:
            print(score,'分不在得分表中')
    elif choice == '4':
        scores.sort(reverse=True)
    else:
        print('输入非法')

input('\n按下回车键退出。')    
    
