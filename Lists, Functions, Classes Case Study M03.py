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

