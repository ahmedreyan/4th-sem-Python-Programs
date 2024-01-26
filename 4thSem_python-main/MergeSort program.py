import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKAgg')
import math
def mergesort(arr):
    if len(arr)==1:
        return arr
    mid=int(len(arr)/2)
    first_half=mergesort(arr[:mid])
    second_half=mergesort(arr[mid:])
    return simplemerge(first_half,second_half)
def simplemerge(L,r):
    i=j=0
    temp=[]
    while i<len(L)and j<len(r):
        if L[i]<r[j]:
            temp.append(L[i])
            i=i+1
        else:
            temp.append(r[j])
            j=j+1
    while i<len(L):
        temp.append(L[i])
        i=i+1
    while j<len(r):
        temp.append(r[j])
        j=j+1
    return temp
arr=[40,80,10,50,30,20,70,60]
print("before sorting: ",arr)
result=mergesort(arr)
print("After sorting:",result)
x=list(range(1,10000))
plt.plot(x,[y*math.log(y,2) for y in x])
plt.title("Merge sort -Time Complexity is O(n log n)")
plt.xlabel("input")
plt.ylabel("Time")
plt.show()
