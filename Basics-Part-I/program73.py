'Write a Python program to calculate midpoints of a line.'

print('\nCalculate the midpoint of a line :')

x1 = float(input('The value of x1 (the first endpoint) '))
y1 = float(input('The value of y1 (the first endpoint) '))

x2 = float(input('The value of x2 (the second endpoint) '))
y2 = float(input('The value of y2 (the second endpoint) '))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2

print('The midpoint of line ({},{}) and ({},{}) is ({},{})'.format(x1,y1,x2,y2,x_m_point,y_m_point))

