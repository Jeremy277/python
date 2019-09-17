import os,signal

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
pid = os.fork()

if pid < 0:
    print('Error')
elif pid == 0:
    print('Child process:',os.getpid())
else:
    print('Parent process')
    while True:
        pass

