'Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.'

num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))
sum = num1 + num2

if sum in range(15,21):
    print('20')
else:
    print('Sum =',sum)