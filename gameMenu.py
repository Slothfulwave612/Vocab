# Vocab's game gameMenu code.
# it will contain all the options the game include.
# the function code will be written in the other file.
# all those codes will be called by importing that file.
# will use the dot-operator to call the functions from file gameFunction.

import time                     # importing time module
from gameFunction import *     # importing gameFunction file to use the functions and imported as gf

obj = Insert_list('', 0, 0, 0, [])

ch = 0                       # ch is the choice, user will specify it's choice
# the program will exit when the user will choose the option 3 which is the exit option

while(ch != 3):
    print()
    time.sleep(0.5)               # stopping time for 0.5 seconds

    print('Vocab Builder !!!'.center(150, ' '))     # printing the title of the project by using center function to allign it in centre

    print()
    time.sleep(0.5)                  # stopping the time for 0.5 seconds

    print('1. Let\'s Play')          # the first option of the program

    time.sleep(0.5)                  # stopping the time for 0.5 seconds

    print('2. View Scores')          # the second option of the program

    time.sleep(0.5)                  # stopping the time for 0.5 seconds

    print('3. Exit')                 # the third option of the program

    while True:
        # try-exception clause
        try:
            print()
            time.sleep(0.5)          # stopping the time for 0.5 seconds

            ch = int(input("Enter The Option Number :- "))
            # for inputting the choice strip() to strip the space from RHS and LHS

            break                    # breaking the clause when the vaild input is inputted by the user

        except ValueError:
            print()
            time.sleep(0.5)         # stopping the time for 0.5 seconds

            print('Invalid Input')  # printing invalid input if the error type - Value-Error

        # now if-elif-else statement will be used to manipulate on the options

    print()
    time.sleep(0.5)             # stopping the time for 0.5 seconds

    if(ch == 1):
        # for option 1 - Let's Play
        obj.LetsPlay()

    elif(ch == 2):
        # for function 2 - View Scores
        obj.scoreTable()

    elif(ch == 3):
        # for option 3 - Exit
        # will break the loop and exit the program
        break

    else:
        # if user entered some wrong option number
        # in this case the program will say the that the option number entered is Invalid
        # and will take you back to the enter the option number again
        continue

# The end of the program...

# Programmed By :- Slothfulwave@612
