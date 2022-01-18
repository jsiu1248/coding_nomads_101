# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random


number=random.randint(1,10)

i=1
while i< 5:
    guess = int(input("Please guess a number between 1 and 10: "))
    i=i+1
    if guess==number and i<5:
        print(f"{number} is the correct number!")
    elif guess!=number and i<5:
        print(f"Sorry try again")
    elif i==5:
        print("Sorry you tried too many times.")
