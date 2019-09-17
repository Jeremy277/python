from multiprocessing import Process,Array,Pipe

# shm = Array('i',[1,2,3,4])
shm = Array('c',b'world')

def fun():
    for i in shm:
        print(i)
    shm[0] = b'W'

# p = Process(target=fun)
# p.start()
# p.join()
# print(shm.value)