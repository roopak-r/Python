#to find sum of digits of a number(sumdigi.py)
n=int(input("Enter the number:"))
s=d=0
while(n!=0):
    d=n%10
    s=s+d
    n=n//10
print("The sum of digits is :",s)                                                                                                                    
