'Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.'

def test(x, y):
    if x ==y or x + y == 5 or abs(x - y) == 5:
        return True
    else:
        return False
num1 = int(input('Enter first number '))
num2 = int(input('Enter second number '))

print(test(num1,num2))
