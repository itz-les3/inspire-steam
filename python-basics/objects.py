#Name: Mark Leslie
#Date: 19/02/2026

# Program to show objects in python

class Human:
    #First we define the attributes of a human being
    type="Mammal"
    legs=2
    brain= True
    warm_blooded= True
    city="Nairobi"

    #we then create a constructor for the class/object
    #The constructor will be used tocreate copies of the object
    def __init__(self,name,age):
       self.human_name= name
       self.human_age= age

    def tell_story(self):
        print(f"Hello,I am {self.human_name}Here is a story")
        print("There was once a bot that said hello world")

#create the humans 
les = Human("les",20)
sanchez =Human("sanchez",27)      

#Let the humans created do things
les.tell_story()
print("les's age is:",les.human_age)