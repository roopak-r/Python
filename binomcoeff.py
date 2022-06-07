#to find binomial coefficient
def fact(m):
    f=1
    for i in range(1,m+1):
        f=f*i
    return f
n=int(input("Enter the value for n:"))
r=int(input("Enter the value for r:"))
s=fact(n)/(fact(r)*fact(n-r))
print("The Answer is:",s)
