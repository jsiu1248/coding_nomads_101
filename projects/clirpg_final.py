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
import random


class Hero:
    def __init__(self):
        self.name=input("What is your name: ")
        self.level=random.randrange(11)

    def attack(self):
        self.level=self.level+10
        return self.level
    def run(self):
        print("You are safe but you ran away from the fight")
class Opponent:
    def __init__(self):
        self.level=random.randrange(11)

    def attack(self):
        self.level=self.level-4
        return self.level


class Weak_Person(Opponent):
    def __init__(self):
        super().__init__()
        self.level=random.randrange(1,5)
        self.name="Brad"
class Final_Boss(Opponent):
    def __init__(self):
        super().__init__()
        self.level=random.randrange(7,11)
        self.name="Devin"

def Room():
    greeting=input(f"Welcome to the game. {hero.name} You have the option between the right or left door Left or Right.")

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
                turn=input("Great. You have a sword. Do you want to turn Left or Right?")
                if turn in ("Left","Right"):
                    action=input("There is a dragon. Do you Fight or Run?")
                    if action=="Fight":
                        if weak.level<=hero.level:
                            print("Go fight the dragon and win!")
                            fight_boss=input("You can fight the boss now. Fight or Run.")
                            if fight_boss=="Fight":
                                if strong.level<=hero.level:
                                    print("Go fight the boss and win!")
                                elif strong.level>hero.level:
                                    print(f"You lost to the boss of level {strong.level} while you had {hero.attack}")
                            elif fight_boss=="Run":
                                print("Good. At least you are still living.")

                        elif weak.level>hero.level:
                            print("You lost to the weakling")
                    elif action=="Run":
                        print("Come on! You could have had a chance")

            if sword =="No":
                print("You will die when you fight the dragon.")
        else:
            raise error
    except: 
        print("Error: Go either Left or Right")

weak=Weak_Person()
strong=Final_Boss()
hero=Hero()
Room()

print(hero.attack())
print(hero.level)
print(weak.level)
print(strong.level)







#https://github.com/martin-martin/python-rpg

#For this project, you are tasked to write a test suite for the CLI game you've been building throughout the course. You can use unittest or pytest for it