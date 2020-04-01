'Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.'

num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))
num3 = int(input('Enter third number '))

if num1 == num2 or num2 == num3 or num1 == num3:
    print('0')
else:
    print(num1+num2+num3)