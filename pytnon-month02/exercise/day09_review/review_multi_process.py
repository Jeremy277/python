#求100000以内所有质数之和
from multiprocessing import Process
from wrapper import timeit
def isprime(n):
    if n<= 1:
        return False
    for i in range(2,int(n)):
        if n%i == 0:
            return False
    return True

#单进程
@timeit
def one_process():
    prime = []
    for i in range(1,100001):
        if isprime(i):
            prime.append(i)
    print(sum(prime))

# one_process()

#多进程 4个
class Prime(Process):
    def __init__(self,prime,begin,end):
        super().__init__()
        self.prime = prime
        self.begin = begin
        self.end = end
    def run(self):
        for i in range(self.begin,self.end):
            if isprime(i):
                self.prime.append(i)
        sum(self.prime)

@timeit
def four_process():
    prime = []
    jobs = []
    for i in range(1,100001,25000):
        p = Prime(prime,i,i+25000)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()

# four_process()

#10进程
@timeit
def ten_process():
    prime = []
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(prime,i,i+10000)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()

ten_process()