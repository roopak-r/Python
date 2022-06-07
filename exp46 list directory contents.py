import os
print(os.getcwd())
print(os.listdir())
dname=input("Enter the name of the new directory:")
os.mkdir(dname)
print(os.listdir())
oname=input("Enter the old name of the directory:")
nname=input("Enter the new name of the directory:")
os.rename(oname,nname)
print(os.listdir())
dname=input("Enter the name of the directory to be deleted:")
os.rmdir(dname)
print(os.listdir())
fname=input("Enter the name of the file:")
if os.path.exists(fname):
    print("File exist")
else:
    print("File doesn't exist")
