class student:
    def __init__(self,rollno1,m1,m2):
        self.rollno = rollno1
        self.mark1 = m1
        self.mark2 = m2
    def sum(self):
        return(self.mark1+self.mark2)
a=int(input("Enter rollno:"))
b=int(input("Enter English mark:"))
c=int(input("Enter Maths mark:"))
p = student(a,b,c)
print('Total mark=',p.sum() )
