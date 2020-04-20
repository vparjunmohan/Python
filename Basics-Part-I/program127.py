'Write a Python program to check whether lowercase letters exist in a string.'


def lowercase():
    for i in string1:
        if ord(i) in range(97, 123):
            return 'There are lowercase letters in the string.'
        else:
            pass

string1 = input('Enter a string: ')
print(lowercase())
