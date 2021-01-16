# Factorial of anumber
a =int(input("Enter the number:")) #Reads Number
fact=1
for i in range (1, a+1):
    fact=fact+i
print("Factorial of", a, "is", fact)
