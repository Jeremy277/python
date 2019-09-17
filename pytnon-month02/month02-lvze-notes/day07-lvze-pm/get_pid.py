"""
获取进程PID号
"""
import os
import time

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    time.sleep(1) # 子进程孤儿
    print("Child PID:",os.getpid())
    print("Get parent PID:",os.getppid())
else:
    time.sleep(30)
    print("Get child PID:",pid)
    print("Parent PID:",os.getpid())
