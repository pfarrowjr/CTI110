# Patrick Farrow
# 9/23/2026
# P1HW2
# 
# Calculates and displays travel expenses

budget = float(input("Enter your budget: "))
destination = input("Enter your destination: ")
gas = float(input("Enter your estimated gas expenses: "))
hotel = float(input("Enter your estimated hotel expenses: "))
food = float(input("Enter your estimated food expenses: "))
total_expenses = gas + hotel + food
remaining_budget = budget - total_expenses

print("-----Travel Expenses-----")
print("Destination:", destination)
print("budget: $", budget)
print("Estimated gas expenses: $", gas)
print("Estimated hotel expenses: $", hotel)
print("Estimated food expenses: $", food)
print("Total expenses: $", total_expenses)
print("Remaining budget: $", remaining_budget)
