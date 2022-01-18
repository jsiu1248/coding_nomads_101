# Use Python's string mini-language to display the table
# that you've built before in a slightly better formatted manner:
#
#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

"""
x=list(range(0,50))
# make fix loops early ten steps
for i in range(0,len(x),10):
    #print('{0:30}'.format(*x[i:i+10]))
    print(*x[i:i+10].__format__())
# access the list then slice 0:10, then 10:20, etc
 #   print('{}'.format(x[i:i+10]))
"""
counter=0
for j in range(0, 50):
    counter=counter+1
    print("{0:^2}".format(j),end=(' ' if counter < 10 else "\n")) #pad with whitespace on both side and align the string at the center
    if counter==10: # didn't know that end can have a condition also.
        counter=0
