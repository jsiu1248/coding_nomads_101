# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

number=int(input("Enter a number between 0 and 1 billion: "))


i=1
while i<(number+1):
    i=i+1
    if i==number:
        print(i)