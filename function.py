import math
# functions
def pythagoras():
    a = input('Enter value for side a: ')
    a = int(a)
    b = int(input('Enter value for side b: '))
    return math.sqrt(a**2 + b**2)
def circle_area():
    radius = int(input('Enter value for radius: '))
    return math.pi * radius**2
def circumference():
    radius = int(input('Enter value for radius: '))
    return 2 * math.pi * radius
def sphere_area():
    radius = int(input('Enter value for radius: '))
    return 4 * math.pi * radius**2
   
# menu
choice = input('''Enter choice:
1 for pythagoras
2 for area of a circle
3 for circumference of a circle
4 for area of a sphere
leave blank to exit: ''')
while choice:
    if choice == '1':
        print(pythagoras())
    elif choice == '2':
        print(circle_area())
    elif choice == '3':
        print(circumference())
    elif choice == '4':
        print(sphere_area())
    else:
        print('Not a valid choice!')


