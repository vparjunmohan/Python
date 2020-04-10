'Write a Python program to calculate body mass index.'

def bmi(height, weight):
    bmi = weight/ (height**2)
    print('Body Mass Index is','%.2f'%bmi)

height = float(input('Enter height in metres '))
weight = float(input('Enter weight in kilogram '))

bmi(height,weight)