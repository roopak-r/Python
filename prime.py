#to check whether a number is prime or not(prime.py)
n=int(input("Enter the number:"))
f=0
for i in range (2,n):
    if(n%i==0):
        f=1
        break
if (f==0):
    print(n,"is prime")
else:
    print(n,"is not prime")
    
   
    
