class publisher:
    def __init__(self,pname):
        self.pname=pname
    def display(self):
        print("name",self.pname)
class Book(publisher):
    def __init__(self,pname,bname,title):
        self.name=pname
        self.bname=bname
        self.title=title
    def display(self):
        print("name",self.pname)
        print("bname",self.bname)
        print("title",self.title)
class python(Book):
    def __init__(self,pname,bname,title,page,price):
        self.pname=pname
        self.bname=bname
        self.title=title
        self.page=page
        self.price=price
    def display(self):
        print("pname",self.pname)
        print("Book",self.bname)
        print("title",self.title)
        print("page",self.page)
        print("price",self.price)

n=input("Enter publisher:")
b=input("Enter book:")
t=input("Enter title:")
p=int(input("Enter pages:"))
pr=int(input("Enter price:"))
obj=python(n,b,t,p,pr)
obj.display()
        
        