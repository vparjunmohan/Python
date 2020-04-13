'Write a Python program to check whether a string is numeric.'

string = input('Enter a String ')

try:
    i = float(string)
    print('It is Numeric')
except (ValueError, TypeError):
    print('It is not Numeric')