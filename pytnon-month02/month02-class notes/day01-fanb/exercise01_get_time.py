#计算列表插入时间
import time
list_01 = list(range(1000000))
start = time.time()
list_01.insert(0,'jer')
end = time.time()
print(list_01)
print(end-start)

#100  time:0.0008254051208496094
#1000 time:0.007929086685180664