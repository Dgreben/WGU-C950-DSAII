# Class containing Package objects to be used in Main.py
class Packages:
    def __init__(self, ID, address, city, state, zipcode, deadline, weight, special_notes, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes
        self.status = status
        self.departure_time = None
        self.delivery_time = None

    # Method to return human-readable information about a Package object
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" %(self.ID, self.address, self.city, self.state, self.zipcode, self.deadline,
                                                    self.weight, self.special_notes, self.status, self.departure_time, self.delivery_time)

    # Method to update the status attribute for a Package object based off of the departure and delivery times
    def update_status(self, time_conversion):
        if time_conversion > self.delivery_time:
            self.status = "Delivered"
        elif time_conversion < self.departure_time:
            self.status = "En Route"
        else:
            self.status = "At Hub"


