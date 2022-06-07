#to read and display a sparse matrix
n=int(input("Enter row size:"))
m=int(input("Enter the column size:"))
x={}
print("Enter the elements of matrix:")
for i in range(n):
    for j in range(m):
        c=int(input("Enter the element:"))
        if c!=0:
            x[i,j]=c
print(x)
print("Matrix is:")
for i in range(n):
    for j in range(m):
        print(x.get((i,j),0),end="")
    print()
