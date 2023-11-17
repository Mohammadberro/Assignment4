# importing json to turn drivers text file into a dictionary
import json


# load list cities from text file
def load_text_city(directory):
    with open(directory, 'r') as f:
        line = f.read()
        cities = line.split(", ")
    return cities


# load drivers as a dictionary from text file
def load_text_drivers(directory):
    with open(directory, 'r') as f:
        lines = f.read()
        new_lines = json.loads(lines)
        drivers = new_lines
    return drivers


# updating drivers whenever we add or modify drivers to our driver's text file
def update_drivers(new_drivers):
    string = json.dumps(new_drivers)
    with open("drivers.txt", 'w') as file:
        file.write(string)


# Add a city to our global list of cities. Avoiding duplicates.
def add_city(city_name):
    if city_name not in cities:
        cities.append(city_name)
        with open("cities.txt", 'w') as file:
            for i in range(0, len(cities)):
                if i == 0:
                    file.write(f"{cities[0]}")
                else:
                    file.write(f", {cities[i]}")
        print(cities)
        print(f"{city_name} was added to the list of cities.")
    else:
        print(f"{city_name} is already in the list of cities.")


# Adding a driver to driver's dictionary. Avoiding duplicates and ensuring valid cities.

def add_driver(driver_name, route):
    if driver_name not in drivers:
        for city in route:
            if city not in cities:
                print(f"The following City:{city} does not exist. Please add it in 'add city' option before adding it "
                      f"to the route")
                return
        drivers[driver_name] = route
        update_drivers(drivers)
        print(f"Driver {driver_name} was added to list of drivers")
    else:
        print(f"Driver {driver_name} is already added to the list of drivers.")


# Adding a city to the driver's(key) route(value). Taking accepted indexes only.

def add_city_to_route(driver_name, city_name):
    if driver_name in drivers:
        if city_name in cities:
            option = input("Enter: \n1. To add the city to the beginning of the route\n-1. To add to the end of the "
                           "route\n#. (any other number) to add that city to the given index.")
            if option.isdigit() or option == "-1":
                option = int(option)
                if option == 1:
                    drivers[driver_name].insert(0, city_name)
                elif option == -1:
                    drivers[driver_name].append(city_name)
                elif 0 <= option < len(drivers[driver_name]):
                    drivers[driver_name].insert(option, city_name)
                else:
                    print("Index is invalid. Please try again and enter a valid index.")
                    return
                update_drivers(drivers)
            else:
                print("Index is invalid. Please try again and enter a valid index.")
        else:
            print(
                f"The city : {city_name} you are trying to add doesn't exist. Please add it before assigning it to the"
                f" driver.")
    else:
        print("Driver's name does not exist in the list of drivers.")


# If the driver and city names exists in our data, this function removes the city and updates the driver's route.
def remove_city_from_route(driver_name, city_name):
    if driver_name in drivers:
        if city_name in drivers[driver_name]:
            drivers[driver_name].remove(city_name)
            update_drivers(drivers)
        else:
            print(f"{city_name} is not listed in the route of {driver_name}")
    else:
        print(f"The following name: {driver_name} does not exist in list of drivers.")


# Check if any driver has the wanted city in his route. Showing results to the user.
def check_deliverability(city_name):
    available_drivers = []
    if city_name in cities:
        for driver, route in drivers.items():
            if city_name in route:
                available_drivers.append(driver)
    if len(available_drivers) > 0:
        print(f"The following drivers can deliver to {city_name}: {available_drivers}")
    else:
        print(f"There are no drivers heading to {city_name}")


# Loading cities and drivers from existing text files.
cities = load_text_city("cities.txt")
drivers = load_text_drivers("drivers.txt")

# Main program.
while True:
    print("Hello! Enter your choice:\n1. To add a city\n2. To add a driver\n3. To add a city to the route of a driver"
          "\n4. To remove a city from a driver's route\n5. To check the availability of a delivery\n")
    option = input("")
    while not option.isdigit() or not (0 < int(option) <= 6):
        option = input("Please enter a valid option\t")
    if option.isdigit() and 0 < int(option) <= 6:
        # Adding a city
        if option == "1":
            city_name = input("\nEnter the Name of the City you want to add.\t")
            # Ensuring valid inputs.
            while not city_name.isalpha():
                city_name = input("Please enter a valid city name\t")
            add_city(city_name)
        # Adding a driver
        elif option == "2":
            driver_name = input("Enter the driver's name?:\t")
            # Ensuring valid inputs.
            while not driver_name.isalpha():
                driver_name = input("Enter the driver's name?:\t")
            route = input("Enter the route of the driver: \t").split()
            add_driver(driver_name, route)

        # Adding a city to a route
        elif option == "3":
            driver_name = input("Enter the driver's name:\t")
            city_name = input("\nEnter the Name of the city you want to add.\t")
            add_city_to_route(driver_name, city_name)
        # Removing a city from a driver's route
        elif option == "4":
            driver_name = input("Enter the driver's name:\t")
            city_name = input("\nEnter the Name of the city you want to add.\t")
            remove_city_from_route(driver_name, city_name)
        # Checking deliverability
        elif option == "5":
            city_name = input("\nEnter the Name of the city you want to deliver to.\t")
            check_deliverability(city_name)
        # Break-exit the program
        elif option == "6":
            print("Exiting the program...")
            break
