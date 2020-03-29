'Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.'

def oddEven():
    if n % 2 == 0:
        print(n,'is an even number')
    else:
        print(n,'is an odd number')

n = int(input('Enter a number '))
oddEven()