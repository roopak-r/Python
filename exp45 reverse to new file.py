fname1=input("Enter the first file name:")
fname2=input("Enter the second file name:")
with open(fname1,'r') as f1,open(fname2,'w')as f2:
    x=f1.readlines()
    for i in range(len(x)):
        f2.writelines(x[i][::-1])
