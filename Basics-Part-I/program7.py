''' Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java'''

filename = input('Enter file name: ')
extension = filename.split('.') 
#split() method returns a list of strings after breaking the given string by the specified separator.

print('Extension of the file',extension[0],'is',extension[1])