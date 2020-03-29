'Write a Python program to get the volume of a sphere with radius r.'

import math

radius = int(input('Enter radius: '))
volume = 4/3*(math.pi*(radius**3))
print('Volume of sphere of radius',radius,'is',volume)