# Create variables answer and SENTINEL for later use
# answer stores withdraw and deposit input values
# SENTINEL used for if user wishes to exit the program
answer = ""
SENTINEL = "E"

print("Welcome to the Automatic Teller Machine. What would you like to do?")
print("For Deposit, press D")
print("For Withdraw, press W")
print("To View Balance, press V")
print("If you wish to Exit, press E")
choice = str(input("What would you like to do?: "))

while choice.upper() != SENTINEL:
    choice = input("This is just a placeholder input. ")

print("Thank you for using our ATM.")