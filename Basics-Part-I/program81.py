'Write a Python program to concatenate N strings.'

def strConcat():
    strlist = string.split(',')
    newStr = ''
    for i in strlist:
        newStr = newStr + i
    print('Concatinated String is',newStr)

string = input('Enter the strings to be concatinated(seperated by commas): ')
strConcat()