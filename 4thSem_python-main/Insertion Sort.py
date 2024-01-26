import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TKAgg")
def insertionsort(a):
    n=len(a)
    for i  in range(1,n):
        k=a[i]
        j=i-1
        while(j>=0 and a[j]>k):
            a[j+1]=a[j]
            j=j-1
            a[j+1]=k
x=[19,78,34,24,48,92,2]
print("Unsorted array is:",x)
insertionsort(x)
print("Sorted array is: ",x)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x])
plt.title("Insertion Sort time complexity is O(Ωn\u00b2)")
plt.xlabel("input")
plt.ylabel("time")
plt.show()

