'Write a Python program to add two objects if both objects are an integer type.'

def add(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        return TypeError('Inputs must be integer')
    else:
        return a + b

print(add(4, 6))