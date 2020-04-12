'Write a Python program to get the size of an object in bytes.'

import sys

val  = input('Enter a string object ')

print("Memory size of '"+val+"' = "+str(sys.getsizeof(val))+ " bytes")

