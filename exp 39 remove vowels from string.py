#to remove
vowels from string
str1=input("Enter a string:")
vowels="aeiouAEIOU"
str2=""
for word in str1:
    if word not in vowels:
        str2+=word
print("The sorted words are:",str2)
