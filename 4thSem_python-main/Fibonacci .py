#Fibonacci
def fib(n):
    if n<=1:
        return n
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    print("The fibonacci sequence is :",f)
    return f[n]
n=int(input("Enter the term:"))
print("The fibonacci value is:",fib(n))
