'Write a Python program to convert the distance (in feet) to inches, yards, and miles.'

def feetConversion():
    inches = feet * 12
    yards = feet / 3
    miles = feet / 5280
    print(feet,'feet is',inches,'inches,','%.2f'%yards,'yards and','%.2f'%miles,'miles.')

feet = int(input('Enter distance in feet: '))
feetConversion()