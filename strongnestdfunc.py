#to find whether a number is strong
def fact(m):
    f=1
    for i in range (1,m+1):
        f=f*i
    return f
def strong (m):
    s=0
    while (m!=0):
        d=m%10
        s=s+fact(d)
        m=m//10
    return s
n=int(input("Enter the number:"))
if(n==strong(n)):
    print(n,"is a strong number")
else:
    print(n,"is not a strong number")
