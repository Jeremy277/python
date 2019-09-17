#练习04
#在控制台获取分钟
#再输入小时
#再输入天
#计算总秒数
#输出结果

minutes = int(input('请输入分钟：'))
hours = int(input('请输入小时：'))
days = int(input('请输入天数：'))
0
seconds = days * 24 * 3600 + hours * 3600 + minutes * 60

print('总秒数为：',seconds,'s。')