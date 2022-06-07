#to print fibonacci series using recursion
def fibo(m):
    if (m==0 or m==1):
        return m
    else:
        return (fibo(m-1)+fibo(m-2))
n=int(input("Enter the range:"))
for i in range (n):
    print(fibo(i),end=" ")
