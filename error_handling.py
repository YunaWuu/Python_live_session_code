# error handling
my_int = input('Enter an integer: ')
while my_int:
    try:
        my_int = int(my_int)
    except ValueError as e:
        print(e)
    my_int = input('Enter an integer: ')
