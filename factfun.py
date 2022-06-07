#to find factorial using function(fact.py)
def fact(m):
    f=1
    for i in range(1,m+1):
        f=f*i
    return f
n=int(input("Enter the number:"))
s=fact(n)
print("The answer is:",s)
