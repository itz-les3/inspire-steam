#Name: Mark Leslie
#Date: 17/02/2026

# Program to perform arithmetic operations in python

num1 = 10
num2 = 5
sum_numbers = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("the sum of the numbers %d" % sum_numbers)
print("quotiont of the numbers %f" % quotient)

#modulus-reminder
print(7%5)

#even and odd numbers
for i in range(1,11):
    if i%2==0:
        print(f"{i} is an even number")
    else:
        print(f"{i} is an odd number")