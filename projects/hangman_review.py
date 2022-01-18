# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it


word="catwalk"
masked='_'*len(word)
print(masked)
print('We are playing hangman. Guess one letter at a time.')
counter=0

num=0
chances=len(word)+3
for i in range(chances):
    guess=input("Guess a letter: ")
    counter=counter+1

    # seeing if there are multiple occurences of a letter
        #things are looping three more times. Why?
    guess_index = word.find(guess, 0)
    #print(f'{guess_index} a')
    if guess not in word:
        print("Letter not found.")
        if chances == 0:
            print("Better luck next time!")
            chances = chances - 1

        continue
    while guess_index > -1:
        #print(guess_index)
        #print(f'{guess_index} b')
        num=guess_index+1
        #print(guess_index)
        masked = masked[0:guess_index] + guess + masked[guess_index + 1:]  # changing the mask
        guess_index=word.find(guess, num)
        #print(f'{guess_index} c')
        if chances == 0:
            print("Better luck next time!")

    print(f"{masked} and you have {chances - counter} chances left")  # subtracting the chances
    if '_' not in masked:
        print(f"Woot! You won! {masked}")



"""
        if word.find(guess, guess_index) != -1:

            masked = masked[0:guess_index] + guess + masked[guess_index + 1:]  # changing the mask
            guess_index=guess_index+1

            if guess_index==-1:

                # if statement that the last loop has happened
                print(f"{masked} and you have {chances - counter} chances left")  # subtracting the chances
            else:
                guess_index=guess_index
                print(guess_index)
        else:
            guess_index = -1

        #index_guess=word.find(guess)
        """

    # else: # this is excuting really fast
    #    print(f"Nope. and you have {chances-counter} chances left")



# if a letter happens twice then it can fill it add
# Allow only single-character alphabetic input