'Write a Python program to check whether a file path is a file or a directory.'

import os  

path = input('Enter a path ')  
if os.path.isdir(path):  
    print('\nIt is a directory')  
elif os.path.isfile(path):  
    print('\nIt is a normal file')  
else:  
    print("File doesn't exist" )
print()