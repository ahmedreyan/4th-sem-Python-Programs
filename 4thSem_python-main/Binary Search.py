#Binary search
def binarysearch(a,key):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(high+low)/2
        if key==a[mid]:
            return mid
        elif(key<a[mid]):
            high=mid-1
        else:
            low=mid+1
        return -1
a=[13,24,56,47,68,79]
print("the array elements:",a)
k=int(input("Enter an element to search:"))
binarysearch(a,k)
if r==-1:
    print("Searching is unsucessful")
else:
    print("Searching  key is found at ",r+1)
