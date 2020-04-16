'Write a Python program to extract the filename from a given path.'

import os

fpath = input('Enter file path ')
print()
print(os.path.basename(fpath))
