#to print fibonacci series upto a n(fibn.py)
n=int(input("Enter the value for n:"))
a=0
b=1
c=0
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

    
