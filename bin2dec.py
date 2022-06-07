#to convert binary number to decimal
def bin2dec(m):
    dec=0
    exp=len(m)-1
    for digit in m:
        dec=dec+int(digit)*2**exp
        exp=exp-1
    return dec
n=input("Enter the binary value:")
decimal=bin2dec(n)
print("The decimal value of", n, "is ", decimal)
