#to find lcm of two numbers
def lcm(a,b):
    if(a>b):
        greatest=a
    else:
        greatest=b
    while(True):
        if((greatest%a==0) and(greatest%b==0)):
            l=greatest
            break
        greatest+=1
    return l
n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
print("The Lcm of", n, "and", m, "is", lcm(n,m))
