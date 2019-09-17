#l练习函数
def rectangle(row,column,char):
    '''
    矩形

    :param row:
    :param column:
    :return:
    '''
    for i in range(row):
        for j in range(column):

            print(char,end=' ')

        print()

rectangle(4,4,'#')
rectangle(4,4,'*')