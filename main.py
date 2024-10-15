# Programmers:  Caitlin Burns and Korede Oni
# Course:  CS151, Professor Zee
# Due Date: 10/16/2024
# Lab Assignment: 5
# Problem Statement:
# Data In:
# Data Out:
# Credits:


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

balance = 1000

while choice.upper() != SENTINEL:
    choice = choice.upper()
    if choice == 'D':
        deposit = int(input("How much would you like to deposit? "))
        while deposit <= 0:
            print('Invalid entry. Try again')
            deposit = int(input("How much would you like to deposit? "))
        balance += deposit
        print(f'Your current balance is ${balance}')
    elif choice == 'W':
        withdraw = int(input("How much would you like to withdraw? "))
        while withdraw <= 0:
            print('Invalid entry. Try again')
            withdraw = int(input("How much would you like to withdraw? "))
        balance -= withdraw
        print(f'Your current balance is ${balance}')
    elif choice == 'V':
        print(f'Your current balance is ${balance}')

    if balance < 0:
        print('Your balance is negative. You will be charged 5% interest')



print("Thank you for using our ATM.")