class Student:
   def __init__(self,rollno,name):
     self.rollno=rollno
     self.name=name
   def dataprint(self):
     print(self.rollno,self.name)
s1=Student(1,"Abin")
s2=Student(2,"Annie")
print("Student Details")
s1.dataprint()
s2.dataprint()
