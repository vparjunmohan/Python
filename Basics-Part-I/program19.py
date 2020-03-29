'Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.'

str = input('Enter a string ')
if str[:2] != 'Is':
    newstr = 'Is' + str
    print('New string is',newstr)
else:
    print('String unchanged',str)
