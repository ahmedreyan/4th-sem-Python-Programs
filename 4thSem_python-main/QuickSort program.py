import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
import math
def partition(array,low,high):
    pivot=array[low]
    left=low+1
    right=high
    while(True):
        while left<right and pivot>array[left]:
            left+=1
        while right>=left and array[right]>pivot:
            right-=1
        if left<right:
                array[left],array[right]=array[right],array[left]
        else:
            break
    array[low],array[high]=array[right],array[low]
    return right
def quick_sort(array,low,high):
    if low>high:
        return array
    else:
        pi=partition(array,low,high)
        quick_sort(array,low,pi-1)
        quick_sort(array,pi+1,high)
array=[10,70,15,8,60,90,20]
print("before sorting: ",array)
quick_sort(array,0,len(array)-1)
print("after sorting: ",array)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("QuickSort Time Complexity is O(n\400b2)")
plt.xlabel("input")
plt.ylabel("Time")
plt.show()
