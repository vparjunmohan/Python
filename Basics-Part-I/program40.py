'Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).'

import math

p1x1 = int(input('Enter x1 coordintes of point 1 '))
p1y1 = int(input('Enter y1 coordintes of point 1 '))
p2x2 = int(input('Enter x2 coordintes of point 2 '))
p2y2 = int(input('Enter y2 coordintes of point 2 '))

distance = math.sqrt((((p2x2-p1x1)**2) + ((p2y2-p1y1)**2)))

print('Distance between (',p1x1,',',p1y1,') and (',p2x2,',',p2y2,') is',distance)