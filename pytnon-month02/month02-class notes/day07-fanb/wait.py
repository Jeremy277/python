import os,sys,time

# try:
#     print('yanzheng')
#     sys.exit(1)
# except SystemExit:
#     print('over')
pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    print('Child process:',os.getpid())
    # time.sleep(10)#此时当子进程不退出时，父进程不会执行，需改进
    os._exit(1)
else:
    pid,status=os.wait()
    print('pid:%s\nstatus:%s'%(pid,status))#状态*256
    while True:
        pass

