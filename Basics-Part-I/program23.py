'Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.'

n = int(input('Enter a non-negative integer '))
str = input('Enter a string ')

if len(str) < 2:
    print(str*n)
else:
    nstr = str[:2]
    print(nstr*n)