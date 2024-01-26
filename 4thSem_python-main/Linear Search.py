def linearsearch(target,key):
    n=len(target)
    for i in range(n):
        if a[i]==key:
            return i;
    return -1
a=[10,30,60,70,36,78,45,76]
print(a)
k=int(input("Enter a number"))
i=linearsearch(a,k)
if i==-1:
    print("target is not found!")
else:
    print("target is  found! at position",i+1)
