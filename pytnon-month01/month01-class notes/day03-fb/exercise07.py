#while 循环
#死循环
while True:

    season = input('请输入季节：')

    if season == '春':
        print('1月2月3月')
    elif season == '夏':
        print('4月5月6月')
    elif season == '秋':
        print('7月8月9月')
    elif season == '冬':
        print('10月11月12月')

    if input('请输入e退出：') == 'e':
        break