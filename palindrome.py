#to check whether a number is palindrome(pali.py)
num=int(input("Enter the number:"))
d=r=0
temp=num
while(temp!=0):
    d=temp%10
    r=(r*10)+d
    temp=temp//10
if (r==num):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")
    
    
   
