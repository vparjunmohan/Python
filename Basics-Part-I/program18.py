' Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum. '

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))

if num1 == num2 == num3:
    print(3*(num1+num2+num3))
else:
    print('Sum of given numbers is',(num1+num2+num3))