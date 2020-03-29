'Write a Python program to get a string which is n (non-negative integer) copies of a given string.'

def copystr():
    copiedStr = ''
    string = input('Enter a string ')
    n = int(input('Enter a number '))
    copiedStr += string * n
    return copiedStr
print(copystr())