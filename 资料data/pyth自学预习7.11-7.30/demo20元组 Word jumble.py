import random
WORDS = ('python','jumble','easy','difficult','answer','iphone')
word = random.choice(WORDS)  #选出要乱序的单词
correct = word
jumble = ''
print(correct)

while word:       #每循环一次，计算机就会创建一个新的word(从Word中去掉一个字母后组成的单词,直到word中为空字符，循环结束)
    position = random.randrange(len(word))     #确定单词长度并乱序
    jumble += word[position]
    word = word [:position] + word[(position + 1):]#去掉position位置后的word

print('欢迎参加有游戏！')
print('乱序后的单词：',jumble)

guess = input('你的答案：')
while guess != correct and guess != '':
    print('猜错了')
    guess = input('你的答案：')
    if guess == correct:
        print('恭喜，答对了')

input('\n按下回车键退出。')
