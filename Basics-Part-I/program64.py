'Write a Python program to get file creation and modification date/times.'

import os.path
import time

def file():
    print('File Created: %s' % time.ctime(os.path.getctime(fname)))
    print('Last Modified: %s' % time.ctime(os.path.getmtime(fname)))

fname = input('Enter file path: ')
file()

#Note: For example Enter file path like C:/Program Files (x86)/Microsoft/Skype for Desktop/Skype.exe