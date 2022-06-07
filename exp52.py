#Employee class implementation (exp. 52)
class Employee:
   empCount = 0
   def __init__(self):
     self.name = input("Enter the name:")
     self.salary = int(input("Enter the salary amount:"))
     Employee.empCount += 1
   def displayCount(self):
     print("Total Employee is:",Employee.empCount)
   def displayEmployee(self):
    print("Name : ", self.name, ", Salary: ", self.salary)
emp1 = Employee()
emp2 = Employee()
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee is",Employee.empCount)
