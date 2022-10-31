class Person:
    #  constructor - initialize and construct person objects
    def __init__(self, firstname, lastname, street, city, state, postcode):
        self.firstname = firstname
        self.lastname = lastname
        self.street = street
        self.city = city
        self.state = state
        self.postcode = postcode

    def __str__(self):
        return f'{self.firstname}, {self.lastname}, {self.street}, {self.city}, {self.state}, {self.postcode}'
        
        