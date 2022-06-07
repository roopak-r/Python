#to count number of lines in a file
def line_count(x):
    with open(x) as f:
        content_list=f.readlines()
        print("The number of lins is:",len(content_list))
fname=input("Enter the file name:")
print(line_count(fname))
