# Name: Mark Leslie
# Date: 16/02/2026
# Program to calculate the factorials of numbers

number =int(input("Enter a number x: ")) #Gets the number of user
factorial = 1 #Initializes  factorial  1
for x in range(0,number):
    factorial = factorial * (x+1) #Calculates the factorial of the number

print(f"The factorial of {number} is: {factorial}")