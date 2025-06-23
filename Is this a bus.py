class Vehicle:
    def __init__(self, name, maxspeed, mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage

class bus(Vehicle):
    pass

schoolbus=bus("school volvo", 180,12)
print("VehicleName:",schoolbus.name,"speed: ", schoolbus.maxspeed, "mileage: ", schoolbus.mileage)
