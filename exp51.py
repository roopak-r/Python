#Rectangle class implementation (exp. 51)
class Rectangle:
    def __init__(self,length,breadth):
     self.length=length
     self.breadth=breadth
    def area(self):
     self.area=self.length*self.breadth
     print(self.area)
r1=Rectangle(10,20)
r1.area()
r2=Rectangle(15,25)
r2.area()
