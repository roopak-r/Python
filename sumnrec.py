#to find sum of n numbers using recursion
def sum(m):
    s=0
    if(m!=0):
        return(m+sum(m-1))
    else:
        return 0
n=int(input("Enter the value of n:"))
print(sum(n))
