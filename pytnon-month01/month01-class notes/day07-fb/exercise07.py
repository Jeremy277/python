#定义将一个序列所有元素打印到终端的功能:
def print_serial(serial):
    '''

    :param num:
    :return:
    '''
    for i in serial:
        print(i,end=' ')

str_1 = 'abcd'
list_1 = [1,2,3,4]
set_1 = {5,6,7,8}
print_serial(set_1)
print_serial(str_1)
print_serial(list_1)
print_serial(set_1)