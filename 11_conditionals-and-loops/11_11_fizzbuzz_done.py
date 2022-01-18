# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number


#display string of 1 to 134


n=list(range(1,135))

for i in range(len(n)+1):
    if i==0:
        print("0", end=" ")
    elif i%15==0:
        print("FizzBuzz", end=" ")
    elif i%3==0:
        print("Fizz", end=" ")
    elif i%5==0:
        print("Buzz", end=" ")
    else:
        print(str(i), end=" ")

