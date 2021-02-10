class bank():
    def __init__(self,acnt,nam,typ,amt):
        self.ac=acnt
        self.name=nam
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("acnt name",self.name)
        print("Acnt num=",self.ac)
        print("acnt type",self.type)
        print("bal",self.amount)
    def with1(self,w1):
        return(self.amount-w1)
n=input("Enter name ")
t=input("Enter type ")

a=int(input("Enter number: "))
am=int(input("Enter amt: "))
obj=bank(a,n,t,am)
print("ACCOUNT DETAILS")
obj.printamt()
w=int(input("Enter amnt to withdraw"))
print("b1",obj.with1(w))

