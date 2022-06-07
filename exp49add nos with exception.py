#to add two numbers with exception handling
fname=input("Enter the file name:")
sum=0
try:
    with open(fname)as f:
        for line in f.readlines():
            wordlist=line.split()
            for word in wordlist:
                number=int(word)
                sum=sum+number
    
except IOError:
    print("There is no file named:",fname)
print("The sum is:",sum)

