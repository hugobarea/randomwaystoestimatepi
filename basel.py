#!/usr/bin/env python3
# basel.py

# Note: After running for 46 hours, pi was estimated correctly to 7 decimal places.

from math import sqrt
from time import *

"""
The following script is based on the Basel problem and Euler's solution to it:
The Basel problem is simply the sum of the inverse of all natural numbers squared. 
Euler found out that thhe exact solution is pi squared over 6.
Using this, and the fact that the sequence converges, through a simple rearrangement of terms it can be seen that the larger the amount of values used,
the better the approximation of pi, up to (in theory) infinite decimal places.

However, a disadvantage of this algorithm is that the series converges extremely slow, so a lot of computational power is needed to get many decimals correct.
Plus, the time taken to run the basel function exponentially increases with the number of terms in the series.
"""


""" TODO:
* Might consider running the timer on a thread, but could decrease efficiency.
* Enhance performance, maybe removing result variable?
* Might run the j loop on a while loop.
"""

def basel(n):
    result = 0

    for i in range (1, n + 1):
        result += 1 / i**2
        
    return sqrt(result * 6)    


if __name__ == '__main__':
    
    start = time()
    nums = 10000000000    # CHANGE THIS

    for j in range (1, nums + 1):
 
        if j % 5000 == 0:   # CHANGE THIS (OPTIONAL)
            print(basel(j))

        if j % 100000 == 0: # CHANGE THIS (OPTIONAL)
            print(f'\nTime elapsed: {strftime("%H:%M:%S", gmtime(time() - start))}')
            print(f'{j:.3e} terms currently being used.\n')