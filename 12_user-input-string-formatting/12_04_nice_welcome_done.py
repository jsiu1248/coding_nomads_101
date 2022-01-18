# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.

first_name=input("What's your name?")
if " " in first_name:
    print("Sorry. Please only use your first name. Too much information!")
else:
    print("Great to meet you!")
