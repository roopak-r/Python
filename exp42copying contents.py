#to copy the contents of a file to another
fname1=input("Enter the first file name:")
fname2=input("Enter the second file name:")
with open(fname1,'r') as f1:
    x=f1.read()
    print(x)
with open(fname2,'w') as f2:
    f2.write(x)
