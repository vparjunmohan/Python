'Write a Python program to input a number, if it is not a number generate an error message.'

try:
    n = int(input('Enter a number '))
except ValueError:
    print('Number should be entered')