# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.

# Display a message that greets them and introduces them to the game world.

# Present them with a choice between two doors.

# If they choose the left door, they'll see an empty room.

# If they choose the right door, then they encounter a dragon.
 
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.

from logging import error


greeting=input("Welcome to the game. You have the option between the right or left door Left or Right.")

try:
    if greeting=="Right":
        print("There is a dragon.")
        dragon=input("Do you wish to fight the dragon? Yes or No.")
        if dragon=="No":
            print("Great choice. You didn't get eaten by the dragon.")
        if dragon=="Yes":
            print("You got eaten because you didn't have a sword.")
    elif greeting=="Left":
        print("The room is empty.")
        sword=input("Actually there is a sword in the room. Do you wish to take it? Yes or No.")
        if sword =="Yes":
            print("Go fight the dragon and win!")
        if sword =="No":
            print("You will die when you fight the dragon.")
    else:
        raise error
except: 
    print("Error: Go either Left or Right")

class Hero:
    def __init__(self,name):
        self.name=input("What is your name: ")

    def attack(self):
        pass
    def run(self):
        pass
class Opponent:
    def __init__(self) -> None:
        pass
    def attack(self):
        pass
# dice for level



# there should be multiple opponents

# Create at least two child classes to your Opponent() class:
# a weak opponent
# a final boss


# Think about what these two child classes should have in common, and where they should differ.
# Implement at least an .attack() method in your Opponent() class, that both of the child classes override in different ways.
# Override the __init__() method of at least one of your two child classes so that it adds another attribute to your child class that the parent class doesn't have.





#https://github.com/martin-martin/python-rpg

#For this project, you are tasked to write a test suite for the CLI game you've been building throughout the course. You can use unittest or pytest for it