#to implement basic calculator(cal.py)
import math
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def power(a,b):
    print(math.pow(a,b))
m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
print("1.Addition\n2.Subtraction\n3.Multiply\n4.Divide\n5.Power")
ch=int(input("Enter your choice:"))
if (ch==1):
    add(m,n)
elif (ch==2):
    sub(m,n)
elif (ch==3):
    mul(m,n)
elif (ch==4):
    div(m,n)
elif (ch==5):
    power(m,n)
else:
    print("Invalid choice")
