#定义函数 根据年月日计算星期几
import time
print('今天星期%d' % int(time.localtime()[6]+1))

def get_week(year,month,day):
    time_tuple = time.strptime('%d/%d/%d' %(year,month,day),'%Y/%m/%d')
    # time_tuple = time.strptime('%d/%d/%d' %
                   # (year, month, day), '%Y/%m/%d')
    week_tuple = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日')
    return week_tuple[time_tuple[6]]
if __name__ == '__main__':
    print(get_week(2019,8,21))
#定义函数 根据生日 计算存活多少天
# now = time.localtime()
# bir = time.strptime("1994/09/05 11:31:30",
#                     '%Y/%m/%d %H:%M:%S')
# print(bir)
