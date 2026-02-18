#Name: Mark Leslie
#Date: 17/02/2026

import math

# Input coefficients
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate discriminant
d = b**2 - 4*a*c

print("\nQuadratic Equation:")
print(f"{a}x² + {b}x + {c} = 0")

# Check nature of roots
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("Two Real and Distinct Roots")
    print("x1 =", x1)
    print("x2 =", x2)

elif d == 0:
    x1 = -b / (2*a)
    print("Two Real and Equal Roots")
    print("x1 =", x1)
    print("x2 =", x1)

else:
    real = -b / (2*a)
    imaginary = math.sqrt(-d) / (2*a)
    print("Complex Roots")
    print("x1 =", real, "+", imaginary, "i")
    print("x2 =", real, "-", imaginary, "i")

   