# Harley Calvert

# Overloading is where two functions have the same name
# but a different parameter list

# Python does not support function overloading
# but we can have a default value if none is specified

# c has a default value 0
def my_function(a,b,c=0):
    return str(a) + str(b) + str(c)


# we can call the function with a different number of arguments
print(my_function(1,1,1))

# the third argument is missing and will default to: 0
print(my_function(1,1))
