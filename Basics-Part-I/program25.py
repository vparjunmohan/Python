'''Write a Python program to check whether a specified value is contained in a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''

def search():
    valList = values.split(" ")
    n =  input('Enter the number to be checked in the list ')
    for i in valList:
        if n == i:
            return True
    return False

values = input('Enter numbers seperated by space ')
print(search())
