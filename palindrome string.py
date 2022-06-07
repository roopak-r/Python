#to check whether a string is palindrome
def palindrome(m):
    if(m==m[::-1]):
        print(m, "is a palindrome string")
    else:
        print(m, "is not a palindrome")
s=input("Enter the string:")
s=s.casefold()
palindrome(s)
