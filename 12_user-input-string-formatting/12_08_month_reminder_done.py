# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.
month=int(input("Enter a number between 1 and 12: "))
if month<=12 and month >=1:
    #print("Please pick a number between 1 and 12.")
    if month ==1:
        print("January")
    elif month ==2:
        print("February")
    elif month ==3:
        print("March")
    elif month ==4:
        print("April")
    elif month ==5:
        print("May")
    elif month ==6:
        print("June")
    elif month ==7:
        print("July")
    elif month ==8:
        print("August")
    elif month == 9:
        print("September")
    elif month ==10:
        print("October")
    elif month ==11:
        print("November")
    elif month ==12:
        print("December")
else:
    print("Seems like the number is not between 1 to 12.")