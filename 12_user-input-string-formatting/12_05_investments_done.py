# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

amount=int(input("Enter amount: "))
interest_rate=float(input("Enter interest rate: "))
years=int(input("Enter years to invest: "))
result=amount*(1+interest_rate)**years
print(f"If you have {amount} and an interest rate of {interest_rate} and invest it for {years} years then you will get {round(result,2)}.")