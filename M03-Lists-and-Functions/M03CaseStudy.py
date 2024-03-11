# Eddie Schaefer
# M03CaseStudy.py
# This program has a vehicle superclass and automobile subclass of it
# vehicle has attributes:
# vehicle type
# automobile has attributes:
# year, make, model, number of doors, type of roof
# app function:
# asks user for each attribute of the car
# then prints them in an easy to read format

# basic vehicle class
class Vehicle():
    def __init__(self, input_type):
        self.type = input_type

class Automobile(Vehicle):
    # initialize the automobile object
    def __init__(self, input_type, input_year, input_make, input_model, input_doors, input_roof):
        # call the superclass to initialize the name
        super().__init__(input_type)
        # initialize the other attributes
        self.year = input_year
        self.make = input_make
        self.model = input_model
        self.doors = input_doors
        self.roof = input_roof
    
    # used to print things nicely at the end
    def printinfo(self):
        # print each attribute value with a nice label
        print("Vehicle type:", self.type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

# ask for each attribute in order
vtype = input('Please enter the type of vehicle: ')

# include the vehicle type as a nice touch
vyear = input(f"Please enter the {vtype}'s year: ")
vmake = input(f"Please enter the {vtype}'s make: ")
vmodel = input(f"Please enter the {vtype}'s model: ")
vdoors = input(f"Does the {vtype} have 2 or 4 doors?: ")
vroof = input(f"Is the {vtype}'s roof solid, or is it a sun roof?: ")

# make automobile object with given data
newvehicle = Automobile(vtype, vyear, vmake, vmodel, vdoors, vroof)
# have it print itself nicely
newvehicle.printinfo()