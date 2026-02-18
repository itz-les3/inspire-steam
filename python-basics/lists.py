#Name :Mark Leslie
#Date :18/02/2026
#Program to show lists in python

friends=["Rachel","Phoebe","Ross","Joel"]

print(friends)
friends.sort()
print(friends)
friends.reverse()
print(friends)
 
friends.append("Jack")
print(friends)

# new list of students
new_friends=["Tracy","James,John,Peter,Val"]
students= friends + new_friends

print(students)
students.pop()
print
students.insert(5,"Jenny")
print(students)
students.insert(9,"Valarie")
students.extend("James")
print(students)

students.remove("Jack")
print(students)

new_students=students.copy()


