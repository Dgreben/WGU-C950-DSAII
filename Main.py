# Author: Dave Greben
# StudentID: 011017178
# DATA STRUCTURES AND ALGORITHMS II — C950 - Task 2

# Required imports for functionality
import csv
import datetime
from Trucks import Trucks
from HashTable import HashTable
from Packages import Packages

# Processing and reading the CSV Files
with open("CSV_Files/Address.csv") as CSV_Address_Raw:
    CSV_Address = csv.reader(CSV_Address_Raw)
    CSV_Address = list(CSV_Address)

with open("CSV_Files/Distance.csv") as CSV_Distance_Raw:
    CSV_Distance = csv.reader(CSV_Distance_Raw)
    CSV_Distance = list(CSV_Distance)

with open("CSV_Files/Package.csv") as CSV_Package_Raw:
    CSV_Package = csv.reader(CSV_Package_Raw)
    CSV_Package = list(CSV_Package)

# Create instance of HashTable using constructor from HashTable.py
package_data_table = HashTable()


# Method to transfer the data from the CSV_Package file to our instance of HashTable
def load_package_data(file, table):
    with open(file, encoding='utf-8-sig') as package_file:
        package_data = csv.reader(package_file)
        # Parse through the CSV_Package file and set each attribute accordingly
        for package in package_data:
            package_id = int(package[0])
            package_address = package[1]
            package_city = package[2]
            package_state = package[3]
            package_zipcode = package[4]
            package_deadline = package[5]
            package_weight = package[6]
            package_status = "At Hub"

            # Create Package object using constructor from Packages.py and attributes from the provided data
            package_object = Packages(package_id, package_address, package_city,
                                      package_state, package_zipcode, package_deadline, package_weight, package_status)

            # Insert the discovered data into the instance of HashTable
            table.insert(package_id, package_object)


# Method to find distance between two given addresses
# Space-Time complexity of O(n)
def distance_between_addresses(x, y):
    distance = CSV_Distance[x][y]
    # Checks the opposite orientation if distance not found
    if distance == '':
        distance = CSV_Distance[y][x]

    # The values in the CSV_Distance file are float values
    return float(distance)


# Method to retrieve address number from the CSV_Address file using the actual address
# Space-Time complexity of O(n)
def retrieve_address(address):
    for row in CSV_Address:
        if address in row[2]:
            return int(row[0])


# Loading packages using the previously defined method into the instance of HashTable
load_package_data("CSV_Files/Package.csv", package_data_table)

# Manually loading all three trucks using the Constructor from Trucks.py
truck_one = Trucks(18, 0.0, 16, [1, 13, 14, 15, 16, 19, 20, 21, 29, 30, 31, 34, 37, 40],
                   "4001 South 700 East", datetime.timedelta(hours=8))

truck_two = Trucks(18, 0.0, 16, [2, 3, 8, 9, 18, 26, 27, 28, 32, 33, 35, 36, 38],
                   "4001 South 700 East", datetime.timedelta(hours=11))

truck_three = Trucks(18, 0.0, 16, [4, 5, 6, 7, 10, 11, 12, 17, 22, 23, 24, 25, 39],
                     "4001 South 700 East", datetime.timedelta(hours=9, minutes=5))


# Method to order packages for a given truck's route based off of the Nearest Neighbor Algorithm
# Space-Time complexity of O(n^2)
def deliver_packages(truck):
    # Add all packages into a designated, empty array
    undelivered = []
    for package_id in truck.packages:
        package = package_data_table.search(package_id)
        undelivered.append(package)

    # Remove the packages from the given truck so that they can be re-added in sorted order
    truck.packages.clear()

    # Cycle through the undelivered array and sort each package by distance
    while len(undelivered) > 0:
        next_package = None
        next_address = 50
        for package in undelivered:
            if next_address >= distance_between_addresses(retrieve_address(truck.location),
                                                          retrieve_address(package.address)):
                next_address = distance_between_addresses(retrieve_address(truck.location),
                                                          retrieve_address(package.address))
                next_package = package

        # Add the next sorted package onto the truck and remove it from the undelivered array
        truck.packages.append(next_package.ID)
        undelivered.remove(next_package)

        # Updates all the necessary attributes for the truck and its respective package
        truck.location = next_package.address
        truck.mileage += next_address
        truck.time += datetime.timedelta(hours=next_address / 18)
        next_package.departure_time = truck.depart_time
        next_package.delivery_time = truck.time


# Begin the delivery process for the first two trucks
deliver_packages(truck_one)
deliver_packages(truck_two)

# Built-in delay for the third truck to satisfy the requirement of only two trucks being active at a time
truck_three.depart_time = min(truck_one.time, truck_two.time)
deliver_packages(truck_three)


# Command Line Interface for the user to browse package and truck data
class Main:
    print("Welcome to the Western Governors University Parcel Service Menu")
    print("The overall mileage for the routes of all the trucks today is:")
    print(truck_one.mileage + truck_two.mileage + truck_three.mileage)

    first_input = input("To begin, please type the word 'start' ")

    # Once the user begins the process, they will be prompted to provide details for the packages they want to see
    if first_input == "start":
        second_input = input(
            "Please enter the time for which you would like to see the status of a package(s). FORMAT: HH:MM:SS ")
        (h, m, s) = second_input.split(":")
        convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        try:
            # The user has an option to browse all packages at the selected time, or just a specific one
            third_input = input("Please enter the Package ID or 'all' ")
            # Space-Time complexity of O(n)
            if third_input == "all":
                # Cycles through each package and prints out the given data
                for packageID in range(1, 41):
                    package = package_data_table.search(packageID)
                    package.update_status(convert_timedelta)
                    print(str(package))

            # If the user inputs a proper ID value, then they will receive the data for that package
            # Space-Time complexity of O(1)
            elif int(third_input) in range(1, 41):
                package = package_data_table.search(int(third_input))
                package.update_status(convert_timedelta)
                print(str(package))

            # The following lines are designed to notify the user if they have made an error with the inputs
            else:
                print("Invalid Entry")
                exit()

        except ValueError:
            print("Invalid Entry")
            exit()
