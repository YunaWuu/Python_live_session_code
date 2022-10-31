# double underscore AKA dunderscore

# unlike Java the instance variables/attributes are accessible and modifiable
# without special functions (getters/accessors, setters/mutators)

class Person():
    # constructor - initialize and construct a person object
    def __init__(self, firstname, lastname, street, city):
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.city = city

    def __str__(self):
        return f'{self.firstname}, {self.lastname}, {self.street}, {self.city}'



# construct a person object, and assign it to the variable p1
# p1 is an instance of the Person class
p1 = Person("Maggie", "Simpson", "742 Evergreen Terrace", "Springfield")

# access the firstname attribute
print(p1.firstname)

# mutate the attribute firstname
# firstname is an instance variable of p1
p1.firstname = "Bart"

# access the firstname attribute, the instance variable
print(p1.firstname)


print(p1)


p2 = Person("Maggie", "Simpson", "742 Evergreen Terrace", "Springfield")

print(p2)
