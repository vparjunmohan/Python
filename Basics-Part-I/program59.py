'Write a Python program to convert height (in feet and inches) to centimeters.'

def convert(feet, inch):
    return float(feet) * 30.48 + float(inch) * 2.54

print('Enter your height\n')
feet = int(input('Enter feet '))
inch = int(input('Enter inch '))
print('Height in centimeteres is',convert(feet,inch),'cm.')