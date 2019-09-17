#快速排序

def sub_sort(l:list,low:int,high:int):
    x = l[low]
    while low < high:
        # while l[high] > x and high > low:
        if l[high] >= x :
            high -= 1
        l[low] = l[high]

        # while l[low] <= x and low < high:
        if l[low] < x :
            low += 1
        l[high] = l[low]
    l[low] = x
    return low

def quick(l:list,low:int,high:int)->None:
    if low < high:
        key = sub_sort(l,low,high)
        quick(l,low,key-1)
        quick(l,key+1,high)


#---------------------------------------
l = [1,2,3,4,3,4,14,5,6,9,45,32,2]
quick(l,0,len(l)-1)
print(l)