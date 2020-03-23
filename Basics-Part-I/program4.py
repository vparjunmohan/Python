"Write a Python program which accepts the radius of a circle from the user and compute the area."

import math

r = float(input('Enter radius of the circle: '))
area = math.pi*r**2
print('Area of the with radius',r,'is',area)