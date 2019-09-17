#访问字典值
# dictionary = {"love": "爱","hate" : "恨"}
# dictionary["love"] 

# print(dictionary["love"])


# if 'hate' in dictionary:
#     print('在字典中')
# else:
#     print('不在字典中')

# print(dictionary.get('hate'))

# 英译汉游戏

dictionary = {"love": "爱","hate" : "恨"}

choice = None

while choice != '0':
    print('''
    英译汉字典
    
    0 - 退出
    1 - 查询
    2 - 添加
    3 - 修改定义
    4 - 删除
    5 - 字典''')

    choice = input('请选择：')

    if choice == '0':
        print('再见')
    elif choice == '1':
        term = input('请输入需要查询的条目：')
        if term in dictionary:
            definition = dictionary[term]
            print('\n%s的汉语是%s' % (term,definition))
        else:
            print('\n查无此项')
    elif choice == '2':
        term = input('请输入需要添加的条目：')
        if term not in dictionary:
            definition = input('请输入该单词的汉语')
            dictionary[term] = definition
            print('\n%s添加完成' % term)
        else:
            print('\n该单词已存在')
    elif choice == '3':
        term = input('请输入需要修改的单词：')
        if term in dictionary:
            definition = input('请输入该单词的汉语：')
            dictionary[term] = definition
            print('\n%s修改完成' % term)
        else:
            print('\n查无此项')
    elif choice == '4':
        term = input('请输入需要删除的条目：')
        if term in dictionary:
            del dictionary[term]
            print('\n%s删除完成' % term)
        else:
            print('\n查无此项')
    elif choice == '5':
        print(dictionary)
        print(dictionary.items())
        print(dictionary.keys())
        print(dictionary.values())
    else:
        print('输入非法，请重新选择')

input('\n按下回车键退出。')
    

