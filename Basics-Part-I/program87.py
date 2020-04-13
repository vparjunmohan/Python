'Write a Python program to get the size of a file.'

import os

fpath = input('Enter file path ')
file_size = os.path.getsize(fpath)
print("\nThe size of file is :",file_size,"Bytes")
print()
