# Patrick Farrow
# 06/27/2026
# P2HW2
# Write a program that asks the user to enter test grades for the following modules, using a separate input statement for each one

# Prompt separately for the grades for Modules 1 through 6.
module1 = float(input("Enter the test grade for Module 1: "))
module2 = float(input("Enter the test grade for Module 2: "))
module3 = float(input("Enter the test grade for Module 3: "))
module4 = float(input("Enter the test grade for Module 4: "))
module5 = float(input("Enter the test grade for Module 5: "))
module6 = float(input("Enter the test grade for Module 6: "))

# Store the grades in a list
grades = [module1, module2, module3, module4, module5, module6]

# Calculate the lowest grade, highest grade, sum of grades, and average grade
lowest_grade = min(grades)
highest_grade = max(grades)
grade_sum = sum(grades)
average_grade = grade_sum / len(grades)

# Display the results
print("-----------results-----------")
print(f"Lowest grade: {lowest_grade}")
print(f"Highest grade: {highest_grade}")
print(f"Sum of grades: {grade_sum}")
print(f"Average grade: {average_grade}")