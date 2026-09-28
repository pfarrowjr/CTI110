# Patrick Farrow
# 06/27/2026
# P2LAB2
# Using dictionaries

cars = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110, 'Silverado': 26}

#Get keys from dictionary
car_keys = cars.keys()

print(car_keys)

print(*car_keys, sep=", ")

#Get a car from user
car_name = input("Enter a car: ")

#Get mpg for given car
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon.")

# Get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

# Calculate
gallons_needed = miles_driven / car_mpg

# Display results
print(f"{gallons_needed:.2f} gallon(s) of gas will be needed to drive the {car_name} {miles_driven} miles.")