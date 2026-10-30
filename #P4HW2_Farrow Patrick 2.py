# Patrick Farrow
# 09/30/2026
# P3HW2
# Salary Calculator with loop

# Request employee info
name = input("Enter employee name (or Done to finish): ")

#Create accumulator variables for overtime pay, regular pay, gross pay and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0


while name != 'done':

    #Add employee count plus 1
    employee_count += 1 # employee_count = employe_count + 1
    #ask for employee infor
    hours = float(input("how many hours did " +name+ " work this week? "))
    rate = float(input("what is " +name+ "'s hourly pay rate? "))

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

    # Add accumulator totals
    overtimepay_total += overtime_pay 
    regularpay_total += regular_pay
    grosspay_total += gross_pay
    


    # Display results for this employee
    print("--------------------------------")
    print(f"Employee Name: {name}")
    print(f'{"Hours worked":<15}{"pay rate":<12}{"Overtime pay":<15}{"Regular pay":<15}{"gross pay":<12}')
    print("--------------------------------")
    print(f"{hours:<15}{rate:<12f}{overtime_pay:<12f}{regular_pay:<15f}{gross_pay:<12f}")



    name = input("Enter employee name (or Done to finish): ")

print("total number of employees entered:, employee_count")
print("total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("total amount paid for regular time: $", format(regularpay_total, '.2f'))
print("total amount paid in gross:$", format(grosspay_total, '.2f'))
