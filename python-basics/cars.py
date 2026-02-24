#Name: Mark Leslie
#Date: 23/02/2026

# program to show classes in python
class car():
    # attributes of car
    def __init__ (self,model,make,color,year):
        self.model = model
        self.make = make
        self.color = color
        self.year = year
    
    #print car details
    def print_details(self,model,make,color,year):
        print(f"{make} {model} of color {color} was manufactured in the year {year}")

   #instantiate a class object
my_car = car("Atenza","Mazda","Red","2022")
dads_car= car("Mistubishi","Outlander","Black","2019")

my_car.print_details("Atenza","Mazda","Red","2022")