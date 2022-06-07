#to sort word
def sortstring(string):
    words=string.split()
    words.sort()
    print("The sorted words are:")
    for w in words:
        print(w)
s=input("Enter the string:")
s=s.casefold()
sortstring(s)
