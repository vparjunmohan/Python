'Write a Python program to remove the duplicate elements of a given array of numbers such that each element appear only once and return the new length of the given array.'


seq = input('Enter elements in the list seperated with commas: ')
listA = seq.split(',')
print('Original List', listA)
setA = set(listA)
newList = list(setA)
print('New List after removing duplicates', newList)
print('Length of new list is', len(newList))
