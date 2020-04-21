'Write a Python program to compute the digit number of sum of two given integers.'

x = int(input('Enter first number '))
y = int(input('Enter second number '))
z = x + y
print('Sum of {} and {} is {} and there are {} digits in the sum'.format(x, y, z, len(str(z))))
