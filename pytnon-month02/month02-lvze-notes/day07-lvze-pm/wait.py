"""
wait.py  处理僵尸进程方法
"""

import os
from time import sleep

pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    print("Child process:",os.getpid()) #子进程pid
    sleep(2)
    os._exit(3) # 进程退出
else:
    pid,status = os.wait() # 阻塞等待回收子进程
    print("pid:",pid)     #退出的子进程pid
    print("status:",os.WEXITSTATUS(status))  #子进程退出状态status: 3
    while True: # 让父进程不退出
        pass
