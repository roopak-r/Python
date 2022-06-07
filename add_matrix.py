#to print sum of two matrix
def read_matrix(m):
    s=[]
    for i in range(m):
        s.append(list(map(int,input().split())))
    return s
def print_matrix(m):
    print(m)
def add_matrix(a,b,m):
    s=[]
    for i in range(m):
        t=[]
        for j in range(m):
            t.append(a[i][j]+b[i][j])
        s.append(t)
    return s
n=int(input("Enter the order of the matrix:"))
print("Enter the elements of first matrix:")
m1=read_matrix(n)
print_matrix(m1)
print("Enter the elements of second matrix")
m2=read_matrix(n)
print_matrix(m2)
print("The sum of",m1,"and",m2,"is",add_matrix(m1,m2,n))
