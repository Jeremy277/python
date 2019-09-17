
# 在目标程序中使用logger来采集错误信息
from rizhi import logger

try:
    1 / 0
except:
    # 等同于error级别，但是会额外记录当前抛出的异常堆栈信息，括号内可以提示哪个模块哪一行
    logger.exception('this is an exception message')
    # logger.error('发生了错误\n')