import os,time


pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    time.sleep(10)
    print('Child PID:',os.getpid())
    print('Get Parent PID:',os.getppid())
else:
    # time.sleep(20)
    print('Get child PID:',pid)
    print('Parent PID:',os.getpid())
    # while True:
    #     pass