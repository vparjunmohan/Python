'Write a Python program to calculate the length of a string.'


def strlen(string):
    length = len(string)
    print('Length of {} is {}'.format(string, length))


string = input('Enter a string ')
strlen(string)
