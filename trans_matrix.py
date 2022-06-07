#to print transpose of a matrix
def read_matrix(m):
    s=[]
    for i in range(m):
        s.append(list(map(int,input().split())))
    return s
def print_matrix(m):
    print(m)
def trans_matrix(a,m):
    s=[]
    for i in range(m):
        t=[]
        for j in range(m):
            t.append(a[j][i])
        s.append(t)
    return s
n=int(input("Enter the order of the matrix:"))
print("Enter the elements of the matrix:")
m1=read_matrix(n)
print_matrix(m1)
print("The transpose of:",m1,"is",trans_matrix(m1,n))
