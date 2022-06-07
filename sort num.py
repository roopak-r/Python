#to sort a list of number
def sort(n):
    a=[]
    for i in range(0,n):
        a.append(int(input()))
    print("Original list is:", a)
    a.sort()
    print("Ordered list is:", a)
x=int(input("Enter the limit:"))
sort(x)
    
 
