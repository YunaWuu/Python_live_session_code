# Harley Calvert

# double underscore AKA dunderscore

# unlike Java the instance variables/attributes are accessible and modifiable
# without special functions (getters/accessors, setters/mutators)

# polymorphism and method overriding
# https://www.edureka.co/blog/polymorphism-in-python/

class Person():
    # constructor - initialize and construct a Person object
    def __init__(self, firstname, lastname, street, city):
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.city = city

    def hello(self):
        return f'Hello {self.firstname}'

    def __str__(self):
        return f'{self.firstname}, {self.lastname}, {self.street}, {self.city}'


class Staff(Person):
    # constructor - initialize and construct a Staff object
    def __init__(self, firstname, lastname, street, city, staff_email, pay_code):
        super().__init__(firstname, lastname, street, city) 
        self.staff_email = staff_email
        self.pay_code = pay_code
        
    def __str__(self):
        return super().__str__() + f', {self.staff_email}, {self.pay_code}'


class Customer(Person):
    # constructor - initialize and construct a Customer object
    def __init__(self, firstname, lastname, street, city, loyalty_number):
        super().__init__(firstname, lastname, street, city) 
        self.loyalty_number = loyalty_number
        
    def __str__(self):
        return super().__str__() + f', {self.loyalty_number}'



# construct a person object, and assign it to the variable maggie
# maggie is an instance of the Person class
maggie = Person("Maggie", "Simpson", "742 Evergreen Terrace", "Springfield")
print(maggie)
print(maggie.hello())

maggie = Staff("Maggie", "Simpson", "742 Evergreen Terrace", "Springfield", "maggie@hotmail.com", "1234")
print(maggie)
print(maggie.hello())

maggie = Customer("Maggie", "Simpson", "742 Evergreen Terrace", "Springfield", "9876")
print(maggie)
print(maggie.hello())
