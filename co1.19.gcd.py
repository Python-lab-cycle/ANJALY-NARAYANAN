# GCD of two numbers
a =int(input("Enter first number:")) #Reads First Number
b =int(input("Enter second number:"))#Reads Second Number
for i in range (1, min(a,b)+1):
    if(a%i==0 and b%i==0): gcd=i
print("GCD of",a ,"and",b, "is",gcd)
