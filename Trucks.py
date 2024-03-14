# Class containing Truck objects to be used in Main.py
class Trucks:
    def __init__(self, speed, mileage, capacity, packages, location, depart_time):
        self.speed = speed
        self.mileage = mileage
        self.capacity = capacity
        self.packages = packages
        self.location = location
        self.depart_time = depart_time
        self.time = depart_time

    # Method to return human-readable information about a Truck object
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s" % (self.speed, self.mileage, self.capacity,
                                         self.packages, self.location, self.depart_time)
