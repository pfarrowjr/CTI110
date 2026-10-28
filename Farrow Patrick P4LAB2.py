#Patrick Farrow
#10/27/2026
#P4Lab2
#Use while loop for loop together

'''
Get integer from the user
Determine if the integer is positive or negative
if number is positive, display multiplication table 
if the number is negative, tell user program to not accept it
Ask user to run again?
if yes, run program
if no, end program
'''

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter a number: "))

    if user_num >= 0:
        #display multiplication for the value range (1-12)
        for item in range(1, 13):
            print(f"{user_num} x {item} = {user_num * item} ")
    else:
        print("This program does not handle negative values ")
    
    run_again = input("Would you like to run the program again? ")

#Loop has broken. User entered 'no' 
print("program is ending....")