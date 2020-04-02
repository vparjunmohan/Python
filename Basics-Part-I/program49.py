'Write a Python program to list all files in a directory in Python.'

import os

def listfiles():
    files  = os.listdir(fdir)
    for file in files:
        print(file)
fdir = input('Enter the directory ')

listfiles()