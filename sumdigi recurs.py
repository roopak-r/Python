#to find sum of digits using recursion
def sumdigi(m):
    if(m!=0):
        return(m%10 + sumdigi(m//10))
    else:
        return 0
n=int(input("Enter the number:"))
print("The sum of digits of", n, "is", sumdigi(n))
