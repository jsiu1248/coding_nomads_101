# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

string_1=input("Enter a string: ")
string_2=input("Enter another string: ")
string_3=input("Enter a third string: ")

if len(string_1) > len(string_2) and len(string_1) > len(string_3):
    print(f"{len(string_1)}, {string_1}" )
elif len(string_2) > len(string_1) and len(string_2) > len(string_3):
    print(f"{len(string_2)}, {string_2}" )

elif len(string_3) > len(string_1) and len(string_3) > len(string_2):
    print(f"{len(string_3)}, {string_3}" )