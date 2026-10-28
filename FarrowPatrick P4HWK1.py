#Patrick Farrow
#10/27/2026
#P4HWK1
#Collect each score, the program will use a loop.



# Ask the user how many scores they want to enter
number_of_scores = int(input("How many scores would you like to enter? "))

# Create an empty list to store valid scores
scores = []

# Use a loop to collect the requested number of valid scores
for count in range(number_of_scores):
    score = float(input(f"Enter score {count + 1}: "))

    # Keep asking until the score is valid
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input(f"Enter score {count + 1}: "))

    # Add the valid score to the list
    scores.append(score)

# Find the lowest score
lowest_score = min(scores)

# Remove one occurrence of the lowest score
scores.remove(lowest_score)

# Calculate the average of the modified score list
average_score = sum(scores) / len(scores)

# Determine the letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print("----------- RESULTS -----------")
print(f"Lowest score dropped: {lowest_score}")
print(f"Score list after dropping lowest score: {scores}")
print(f"Average after dropping lowest score: {average_score:.2f}")
print(f"Letter grade: {letter_grade}")