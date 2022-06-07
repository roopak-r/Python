#to find hcf of two numbers
def hcf(a,b):
    if a>b:
        small=b
    else:
        small=b
    for i in range(1,small+1):
        if((a%i==0) and (b%i==0)):
            h=i
    return h
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
print("The hcf of", n ,"and", m, "is", hcf(n,m))
