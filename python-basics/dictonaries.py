#Name: Mark Leslie
#Date: 1/082/2026

# Program to show dictionaries in python

car={"Model":"Dodge","Make":"Mustang","color":"Black","year":"2025"}
print(car)

print(car["Model"])
print(car["year"])

students={"Alice":20,"James":18,"Mark":22}

for key in students:
    print(key)

for val in students.values():
    print(val)