# Patrick Farrow
# 06/30/2026
# P3HW1
# This program takes six module grades, calculates their average, and displays the corresponding letter grade.


# Enter grades for six modules
module1 = float(input("Enter the grade for Module 1: "))
module2 = float(input("Enter the grade for Module 2: "))
module3 = float(input("Enter the grade for Module 3: "))
module4 = float(input("Enter the grade for Module 4: "))
module5 = float(input("Enter the grade for Module 5: "))
module6 = float(input("Enter the grade for Module 6: "))

# Add the grades entered to a list
grade = [module1, module2, module3, module4, module5, module6]

# Determine the lowest, highest, sum, and average
low = min(grade)
high = max(grade)
total = sum(grade)
avg = total / len(grade)

print("-----------results-----------")
print(f"Lowest grade: {low}")
print(f"Highest grade: {high}")
print(f"Total of grades: {total}")
print(f"Average grade: {avg:.2f}")

# Determine the letter grade for the average

print("----------------------")
if avg >= 90:
    letter_grade = "A"
elif avg >= 80:
    letter_grade = "B"
elif avg >= 70:
    letter_grade = "C"
elif avg >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Your grade is: {letter_grade}")





