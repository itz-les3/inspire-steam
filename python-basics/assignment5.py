#Name: Mark Leslie
#Date: 17/02/2026

# Program to display diamond and triangle

# Ask user for number of rows
n = int(input("Enter the number of rows: "))

print("\nTriangle Pattern:\n")

# Triangle
for i in range(1, n + 1):
    print("*" * i)

print("\nDiamond Pattern:\n")

# Upper half of diamond
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Lower half of diamond
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

