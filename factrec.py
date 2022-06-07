#to find factorial using recursion
def fact(m):
    if(m==0):
        return 1
    else:
        return m*fact(m-1)
n=int(input("Enter the number:"))
facto=fact(n)
print("Factorial=",facto)
