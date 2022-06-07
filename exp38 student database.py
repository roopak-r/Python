#student database using dictionary
num_students=int(input("Please enter number of students:"))
print("You entered",num_students,"students")
student_info={}
student_data=['Math marks:','Physics marks:','Computer marks:']
for i in range(0,num_students):
    student_name=input("Name:")
    student_info[student_name]={}
    for entry in student_data:
        student_info[student_name][entry]=int(input(entry))
print("Please enter student name:")
name=input("Student name:")
if name in student_info.keys():
    print("Average marks:",str(sum(student_info[name].values())/3.0))
else:
    print("please enter a valid name")
        
