from curses.ascii import isdigit
from person import Person

firstname = ''
lastname = ''
street = ''
city = ''
state = ''
postcode = ''
people = []  # list of person objects

with open('data_files/largeData.dat') as data:
    lines = data.readlines()

for line in lines:
    if ',' in line:
        lastname, firstname = line.strip().split(', ')

    elif line[0].isdigit():
        street = line.strip()

    elif '\t' in line:
        city, state, postcode = line.strip().split('\t')
    
    else:
        # construct person object
        person = Person(firstname, lastname, street, city, state, postcode)
        people.append(person)  # add person objects to list

# sort the list of person objects by lastname
people.sort(key=lambda peson: person.lastname, reverse=False)

for person in people:
    print(person)

# with open('data_files/largeData.csv', 'w') as out:
#     for person in people:
#         out.write(str(person) + '\n')