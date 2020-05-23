'Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).'

words = input('Enter comma seperated sequence of words: ')
lwords = words.split(',')
print(sorted(list(set(lwords))))