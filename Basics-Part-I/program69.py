'Write a Python program to sort three integers without using conditional statements and loops.'

x = int(input('Enter first number '))
y = int(input('Enter second number '))
z = int(input('Enter third number '))

a = min(x,y,z)
b = max(x,y,z)
c = (x+y+z)-(a+b)

print('Sorted order is',a,c,b)