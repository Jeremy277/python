import time

#获取当前时间戳  从1970年1月1日到现在的总秒数
print(time.time())#1566385830.1379533
#获取当前的时间元组
#(年 月 日 时 分 秒 一周的第几天(0 1 2...) 一年的第几天 夏令时)
print(time.localtime())#time.struct_time(tm_year=2019, tm_mon=8,.....)
#获取指定时间戳的时间元组
print(time.localtime(12345678))#time.struct_time(tm_year=1970, ...)
time_tuple = time.localtime()
#将时间元组变成时间戳
print(time.mktime(time_tuple))#1566386031.0


#将时间元组转换成时间字符串
print(time.strftime('%y/%m/%d %H:%M:%S',time_tuple))#19/08/21 19:17:07
print(time.strftime('%Y-%m-%d %H:%M:%S',time_tuple))#2019-08-21 19:17:07

#将日期字符串转换为时间元组
print(time.strptime("19/08/21 11:31:30", '%y/%m/%d %H:%M:%S'))#time.struct_time(tm_year=2019, tm_mon=8,.....)
print(time.strptime("2019/08/21 11:31:30", '%Y/%m/%d %H:%M:%S'))

print('开始运行')
time.sleep(5)
print('程序结束')







