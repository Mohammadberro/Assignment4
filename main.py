def save_text(directory):
    with open(directory, 'r') as f:
        for line in f:
            cities = line.split(", ")
    return cities


def save_text_drivers(directory):
    drivers = {}
    with open(directory, 'r') as f:
        for line in f:
            (key, val) = line.split()
            drivers[key] = val
    return drivers


# Created a list of cities that initially contains the most populated cities in Lebanon.
# More ciities can be added during the Main Program


# Creating an empty dictionary of drivers, which will be used to store drivers and their route.


# We call this function to add a city to our global list of cities.
# Note that a city will only be added if the city name is not already in the list, avoiding duplicate city names.
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


# We call this funtion to add a new driver to drivers dictionary.
# Note that a new driver name will only be added if the name does not exist, so that a driver doesn't get added twice.
# Any city in the route should be among our global list of cities, insuring additional validation.

def add_driver(driver_name, route):
    if driver_name not in drivers:
        for city in route:
            if city not in cities:
                print(f"The following City:{city} does not exist. Please add it in 'add city' option before adding it "
                      f"to the route")
                return
        drivers[driver_name] = route
        print(f"Driver {driver_name} was added to list of drivers")
    else:
        print(f"Driver {driver_name} is already added to the list of drivers.")


# We call this funtion to add a city to the driver's(key) route(value).
# First we make sure the driver's and city's names are valid to avoid errors and ensure validation.
# The option represents the index of the route , so we make sure that the option is a digit.
# Any option that does not represent the index of the route will not be processed.(not between -1 and len(route_list))

def add_city_to_route(driver_name, city_name):
    if driver_name in drivers:
        if city_name in cities:
            option = input("Enter: \n1. To add the city to the beginning of the route\n-1. To add to the end of the "
                           "route\n#. (any other number) to add that city to the given index.")
            if option.isdigit():
                option = int(option)
                if option == 1:
                    drivers[driver_name].insert(0, city_name)
                elif option == -1:
                    drivers[driver_name].append(city_name)
                elif 0 <= option < len(drivers[driver_name]):
                    drivers[driver_name].insert(option, city_name)
            else:
                print("Index is invalid. Please try again and enter a valid index.")
        else:
            print(
                f"The city : {city_name} you are trying to add doesn't exist. Please add it before assigning it to the"
                f" driver.")
    else:
        print("Driver's name does not exist in the list of drivers.")


def remove_city_from_route(driver_name, city_name):
    if driver_name in drivers:
        if city_name in drivers[driver_name]:
            drivers[driver_name].remove(city_name)
        else:
            print(f"{city_name} is not listed in the route of {driver_name}")
    else:
        print(f"The following name: {driver_name} does not exist in list of drivers.")


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


cities = save_text("cities.txt")
drivers = save_text_drivers("drivers.txt")
while True:
    print(f"{cities}, \n{drivers}")
    print("Hello! Enter your choice:\n1. To add a city\n2. To add a driver\n3. To add a city to the route of a driver"
          "\n4. To remove a city from a driver's route\n5. To check the availability of a delivery")

    option = input("What do you want to do?\t")
    if option.isdigit() and 0 < int(option) <= 6:
        if option == "1":
            city_name = input("\nEnter the Name of the City you want to add.\t")
            if city_name.isalpha():
                add_city(city_name)
            else:
                city_name = input("Please enter a valid city name\t")

        elif option == "2":
            driver_name = input("Enter the driver's name?:\t")
            route = input("Enter the route of the driver: \t").split()
            add_driver(driver_name, route)

        elif option == "3":
            driver_name = input("Enter the driver's name:\t")
            city_name = input("\nEnter the Name of the city you want to add.\t")
            add_city_to_route(driver_name, city_name)

        elif option == "4":
            driver_name = input("Enter the driver's name:\t")
            city_name = input("\nEnter the Name of the city you want to add.\t")
            remove_city_from_route(driver_name, city_name)
        elif option == "5":
            city_name = input("\nEnter the Name of the city you want to deliver to.\t")
            check_deliverability(city_name)
        elif option == "6":
            print("Exiting the program...")
            break
    else:
        print("Please enter a valid option")
