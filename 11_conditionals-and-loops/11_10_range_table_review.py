# Read up on `range()` and additional options for `print()`.
# Then use a loop to print the following table to the console:
#
# 0 1 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

# five loops
#have to make x with a list. Range can't be stand alone.
# len(x) because it can't iterate a list and needs to be a number
x=list(range(0,50))
# make fix loops early ten steps
for i in range(0,len(x),10):
# access the list then slice 0:10, then 10:20, etc
    print(x[i:i+10])

