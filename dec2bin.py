#toconvert decimal to binary
def dec2bin(m):
    if(m==0):
        return 0
    else:
        bin=" "
        while(m!=0):
            r=m%2
            bin=str(r)+bin
            m=m//2
        return bin
d=int(input("Enter a decimal number:"))
binary=dec2bin(d)
print("The binary value of", d, "is", binary)   
