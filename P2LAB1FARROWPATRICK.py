# Patrick Farrow
# 9/23/2026
# P2LAB1
# This program calculates the diameter, circumference, and area of a circle. 

# import the math module to use the constant, math.pi
import math

# Get radius from user
radius = float(input("What is the radius of the circle: "))
print()

#calculate the diameter
diameter = 2 * radius

# display diameter with 1 decimal place
print(f"the diameter of the circle is: {diameter:.1f}")

# Calculate circumfrence
circumference = 2 * math.pi * radius

#Display circumference with 2 decimal places
print(f"the circumference of the circle is: {circumference:.2f}")

# Calculate area
area = math.pi * radius ** 2

#display area with 3 decimal places
print(f"the area of the circle is: {area:.3f}")