#刽子手游戏
#经典猜字游戏，计算机随机选取一个单词，玩家想办法将他一个字母一个字母猜出来
#如果玩家没能及时猜出是哪个单词，火柴小人就会被吊死。
import random

#创建常量
HANGMAN = ('''
----
|   |
|   
| 
|  
|   
|  
|   
|
----------
''',
'''
----
|   |
|   o
| 
|  
|  
| 
| 
|
----------
''',
'''
----
|   |
|   o
| /-+-/
|   
|   
|   
|    
|
----------
''',
'''
----
|   |
|   o
| /-+-/
|   |
|   
|    
|   
|
----------
''',
'''
----
|   |
|   o
| /-+-/
|   |
|   |
|  
|    
|
----------
''',
'''
----
|   |
|   o
| /-+-/
|   |
|   |
| |   |
|    
|
----------
''',
'''
----
|   |
|   o
| /-+-/
|   |
|   |
| |   |
| |   
|
----------
''',
'''
----
|   |
|   o
| /-+-/
|   |
|   |
| |   |
| |   |
|
----------
''')

MAX_WRONG = len(HANGMAN) - 1
WORDS = ('LOVE','HATE','HAPPY','SAD','LUCKY')

#初始化变量

word = random.choice(WORDS)
so_far = '_' * len(word)
wrong = 0
used = []

print(word)

#创建主循环
print('欢迎参加刽子手游戏！')

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print('\n你已经猜过的字母：\n:',used)
    print('\n到目前位置，已经猜出的部分：\n',so_far)

    #获取用户答案
    guess = input('\n请输入你的答案：')
    guess = guess.upper()

    while guess in used:
        print('你应经猜过这个字母了',guess)
        guess = input('\n请输入你的答案：')
        guess = guess.upper()

    used.append(guess)

    #判断结果
    if guess in word:
        print('\n你猜对了',guess,'在秘钥单词中')
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print('\n',guess,'不在秘钥单词中')
        wrong += 1

#结束程序
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print('\n你已经被绞死了！')
    print('\n秘钥单词是',word)
else:
    print('你猜对了！')

print('\n秘钥单词是',word)

input('\n按回车键退出！')
