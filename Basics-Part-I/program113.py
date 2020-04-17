'Write a Python program to filter the positive numbers from a list.'
n = input('Enter list of numbers seperated by commas ')
newList = n.split(',')
positiveList = list()

for i in newList:
    if int(i) > 0:
        positiveList.append(i)
print('Positive Numbers in the list are',positiveList)