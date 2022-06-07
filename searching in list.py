#to search a given number in a list
def search(n):
    a=[]
    for i in range(0,n):
        a.append(int(input()))
    x=int(input("Enter the number to be searched:"))    
    print("Original list is:", a)
    if x in a:
        print(x, "is found at position", a.index(x))
    else:
        print(x, "is not found")
n=int(input("Enter the limit:"))
search(n)
