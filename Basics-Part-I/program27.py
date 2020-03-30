'Write a Python program to concatenate all elements in a list into a string and return it.'

def concatList(elementList):
    elementSplit = elementList.split(' ')
    newStr = ''
    for i in elementSplit:
        newStr += i
    return newStr

elementList = input('Enter items for the list seperated by space ')
print(concatList(elementList))