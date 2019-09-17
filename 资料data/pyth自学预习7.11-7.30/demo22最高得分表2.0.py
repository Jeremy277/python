#最高得分表2.0 嵌套序列

scores = []
choice = None

while choice != '0':
    print('''
    最高得分表
    
    0 - 退出
    1 - 得分表
    2 - 添加得分''')

    choice = input('请选择：')

    if choice == '0':
        print('再见')
    elif choice == '1':
        print('最高得分表')
        print('姓名\t得分')
        for entry in scores:
            score, name = entry
            print(name, '\t', score)
    elif choice == '2':
        name = input('选手姓名：')
        score = int(input('选手得分：'))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5]
    else:
        print('输入非法')

input('\n按下回车键退出。')    
    