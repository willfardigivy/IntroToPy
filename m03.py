class Vehicle():
    def __init__(self, vtype):
        self.type = vtype

class Automobile(Vehicle):
    def __init__(self, ayear, amake, amodel, adoors, aroof):
        self.year = ayear
        self.make = amake
        self.model = amodel
        self.doors = adoors
        self.roof = aroof
        Vehicle.__init__(self,type)

    def printstuff(self):
        print(f"Vehicle Type: {self.type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of Doors: {self.doors}")
        print(f"Roof Type: {self.roof}")

type = input("Please input the type of vehicle: ")
year = int(input("Please provide the year: "))
make = input("Please provide the make: ")
model = input("Please provide the model: ")
doors = int(input("Please provide the number of doors: "))
roof = input("Please provide the type of roof: ")

info = Vehicle(type)
info = Automobile(year, make, model, doors, roof)

info.printstuff()