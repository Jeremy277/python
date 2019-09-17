#练习在控制台获取一个季节（春夏秋冬）
# 显示相应月份

season = input('请输入季度：')
#方法一
if season == '春':
    print('1月2月3月')
if season == '夏':
    print('4月5月6月')
if season == '秋':
    print('7月8月9月')
if season == '冬':
    print('10月11月12月')

#方法二  调试方法一和方法二 观察区别

if season == '春':
    print('1月2月3月')
elif season == '夏':
    print('4月5月6月')
elif season == '秋':
    print('7月8月9月')
elif season == '冬':
    print('10月11月12月')