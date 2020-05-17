'Write a Python program to remove the nth index character from a nonempty string.'

string = input('Enter a string: ')
char = int(input('Enter the index to be removed: '))  
new = string[0:char] + string[char+1:]

print('New String is',new)
