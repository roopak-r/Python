#to enter a matrix
def matrix(n):
    print("Start entering values:")
    n=[]
    for j in range(0,2):
        n1=[]
        print("Enter the values in", j, "th", "row:")
        for i in range(0,2):
             n1.append(int(input()))
        n.append(n1)
    print(n)
def addition(a,b):
    n=[]
    for i in range(0,2):
        n=[]
        for j in range(0,2):
            n.append((a[i][j])+(b[i][j]))
    print(n)        
m=[]
x=[]
matrix(m)
matrix(x)
addition(m,x)
print(addition(m,x))

    
    
