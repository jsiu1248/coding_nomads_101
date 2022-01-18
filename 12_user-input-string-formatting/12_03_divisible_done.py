# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
number=int(input("Pick a number between 1 and 1 billion and I will see if it is divisible by 3: "))

if number%3==0 and number>=1 and number<=1000000000:
    print(f"{number} is divisble by 3")
else:
    print("Try again")
