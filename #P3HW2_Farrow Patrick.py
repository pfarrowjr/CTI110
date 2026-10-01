# Patrick Farrow
# 09/30/2026
# P3HW2
# Salary Calculator

# Request employee info
name = input("Enter employee name: ")
hours = float(input("Enter number of hours worked: "))
rate = float(input("Enter hourly pay rate: "))

# Evaluate overtime
if hours > 40:
    # Calculate overtime 
    overtime_hours = hours - 40
    # Calculate over pay
    overtime_pay = overtime_hours * (rate * 1.5)
    # Calculate salary for regular hours
    regular_pay = 40 * rate
    # Calculate gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

# Display results
print("--------------------------------")
print(f"Employee Name: {name}")
print(f'{"Hours worked":<15}{"pay rate":<12}{"Overtime pay":<15}{"Regular pay":<15}{"gross pay":<12}')
print("--------------------------------")
print(f"{hours:<15}{rate:<12f}{overtime_pay:<12f}{regular_pay:<15f}{gross_pay:<12f}")
