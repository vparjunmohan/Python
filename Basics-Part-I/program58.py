'Write a python program to find the sum of the first n positive integers.'

def nsum():
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

n = int(input('Emter positive integer '))
print('Sum =',nsum())