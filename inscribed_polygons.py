#!/usr/bin/env python3
# inscribed_polygons.py

''' NOTE: After less than 10min of runtime, the script finds successfully the first 15 decimals, but seems to stop there, probably because
of the limitations that are involved due to the use of the math.radian function required to use math.sin (math.sin only works with radians).
As converting from degrees to radians involves multiplying by pi and dividing by 180, the accuracy of the angle in radians will be limited by
the estimation of pi in the math module.
'''
from math import sin, radians
from time import *

if __name__ == '__main__':
    n = 1
    start = time()

    while True:
        pi = n / 2 * sin(radians(360/n))
        
        if n % 1000000 == 0:
            print(f'\nTime elapsed: {strftime("%H:%M:%S", gmtime(time() - start))}')
            print(f'The inscribed polygon has {n:.3e} sides.\n')
            print(pi)

        n += 1
    