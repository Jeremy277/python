# ﻿1.在控制台获取输入的月份 显示对应的季度 或提示月份错误

month = int(input('请输入月份（1-12）：'))
#简化比较逻辑，前述以判断的，无需再判断
if month < 0 or month > 12:
    print('输入月份错误！')
elif  month <= 3:
    print('%d月是春季' % month)
elif  month <= 6:
    print('%d月是夏季' % month)
elif  month <= 9:
    print('%d月是秋季' % month)
else:
    print('%d月是冬季' % month)
