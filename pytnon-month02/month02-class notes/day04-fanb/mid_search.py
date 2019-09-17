#二分法查找：

def search(l,val):
    low,high = 0,len(l) - 1
    while low <= high:
        mid = (low+high) // 2
        if l[mid] < val:
            low = mid +1
        elif l[mid] > val:
            high = mid -1
        else:
            return mid

l = [1,2,3,4,5,6,7,8,10,11,56,78,99,100]
print(search(l,1))