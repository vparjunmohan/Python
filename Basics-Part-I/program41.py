'Write a Python program to check whether a file exists.'

import os

def filecheck():
    return os.path.isfile(fname) #isfile() is used to check whether the specified path is an existing regular file or not. Returns True if file exists.

fname = input('Enter file name ')
print(filecheck()) 