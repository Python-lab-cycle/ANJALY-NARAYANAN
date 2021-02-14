#Function to find all the factors of a number
def factors(a):
 for i in range (1,(a+1)):
    if (a%i==0) : print(i)
 return;
#Main Function
a=int(input("Enter a Number:"))
factors(a)#Function calling
