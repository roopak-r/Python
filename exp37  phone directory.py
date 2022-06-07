#telephone dictionary using dictionary
def print_menu():
    print("1. Print phone numbers")
    print("2. Add a phone number")
    print("3. Remove a phone number")
    print("4. Lookup a phone number")
    print("5. Quit")
    print()
numbers={}
menu_choice=0
print_menu()
while menu_choice!=5:
    menu_choice=int(input("Type in a number (1-5)"))
    if menu_choice==1:
        print("Telephone numbers:")
        for x in numbers.keys():
            print("Name:",x,"\tNumber:",numbers[x])
        print()
    elif menu_choice==2:
        print("Add name and number:")
        name=input("Name:")
        numbers[name]=input("Number:")
    elif menu_choice==3:
        print("Remove Name and number")
        name=input("Name:")
        if name in numbers:
            del numbers[name]
        else:
            print(name,"Not Found")
    elif menu_choice==4:
        print("Look up number")
        name=input("Name:")
        if name in numbers:
            print("The number is:",numbers[name])
        else:
            print(name,"Not Found")
    elif menu_choice!=5:
        print_menu()
        
