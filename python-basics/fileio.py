#Name: Mark Leslie
#Date: 24/02/2026

#program to perform file operations 

#create a new file
newfile = open("student-data.txt","a")

#write to new file
newfile.write("{student Name: Mark Leslie,ID: 12345,email: mark.leslie@inspire.org}")
#close the file
newfile.close()

#read the file
newfile = open("student-data.txt","r")
print(newfile.read())
#close the file
newfile.close()

#delete the file
import os
os.remove("student-data.txt")
