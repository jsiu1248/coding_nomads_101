
# Print out every prime number between 1 and 1000.

import math
n=1001
for i in range(2,n):
    prime=True
    #setting all of them prime=True first
    for j in range(2,i):
        #for each number the range is different. So, the number 3 starts with 2 and ends with 3.
        if ( i % j==0):
            #9/2 doesn't change. But, 9/3 changes to prime is false
            prime=False
    if prime:
        #if it is prime then print it
        print(i)

        #2,3,5,7,11


