my_string = 'the quick brown fox'
for letter in my_string:
    print(type(letter))
for index, letter in enumerate(my_string):
    print(index, letter)
# string splicing
print(my_string[16:])   # goto end of string
print(my_string[4:9])   # from 4 to 9 exclusive
print(my_string[:3])    # from start to 3 exclusive