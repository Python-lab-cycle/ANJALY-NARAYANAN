import math
class circle():
    def __init__(self,radius):
        self.radius1=radius
    def area(self):
        return(self.radius1*self.radius1*math.pi)
a=int(input("Enter radius of circle:"))
obj=circle(a)
print("Area of circle:",obj.area())
