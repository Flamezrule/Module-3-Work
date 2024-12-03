#Alexander Eyermann
#12/3/2024
#This program uses a class to hold Vehicle information in automobile. This is contained within a superclass but is just being assigned to car.
#The class holds the information on a vehicle and the ability to display that held info
#The user will be asked to enter in 5 prompts about their car, and then it will be given back to them through the info stored in the class

class Vehicle:
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

class Automobile(Vehicle):
    def __init__(self, vehicleType, year, make, model, doors, roof):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def displayInfo(self):
        print(f"Vehicle type: {self.vehicleType}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of Doors: {self.doors}")
        print(f"Type of Roof: {self.roof}")

print("Please Enter the details of your car")

    #Instructions say to just make the vehicle Type be Car
vehicleType = "Car"

year = input("Enter the year of your car: ")
make = input("Enter the make of your car: ")
model = input("Enter the model of your car: ")
doors = input("Enter the number of doors in your car (2 or 4): ")
roof = input("Enter the type of roof in your car (Solid or Sunroof): ")

Car = Automobile(vehicleType, year, make, model, doors, roof)

print("Car Details: ")
Car.displayInfo()

