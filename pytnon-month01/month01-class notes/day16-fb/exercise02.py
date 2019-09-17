#定义函数 输入成绩  若异常继续输入 正确为止
def get_score():
    while True:
        try:
            score = int(input('请输入学生成绩:'))
            return print('张楠的成绩为%d分' % score)
        except:#默认所有异常
            print('输入有误')



if __name__ == '__main__':
    get_score()
