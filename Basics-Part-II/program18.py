' Write a Python program to find the median among three given numbers.'

x = int(input('Enter first number '))
y = int(input('Enter second number '))
z = int(input('Enter third number '))

numList = [x, y, z]
sortedNum = sorted(numList)
print('Median of above three numbers is', sortedNum[1])
