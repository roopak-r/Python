#floyd triangle
n=int(input("enter the number:"))
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end="\t")
        a=a+1
    print()    
