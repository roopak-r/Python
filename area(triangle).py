#Area of triangle(area.py)
a=float(input("Enter the first side:"))
b=float(input("Enter the second side:"))
c=float(input("ENter the third side:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area is:",area)
