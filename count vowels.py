#to count vowels in a string
def countvowels(string):
    count=0
    for char in string:
        if char in "aeiou":
            count=count+1
    return count
s=input("Enter the string:")
s=s.casefold()
print("The number of vowels=", countvowels(s))
