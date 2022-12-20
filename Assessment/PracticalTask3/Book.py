class Book:
    # construstor
    def __init__(self, isbn, title, authorFirstName, authorLastName, price):
        self.isbn = isbn
        self.title = title
        self.authorFirstName = authorFirstName
        self.authorLastName = authorLastName
        self.price = price

    def __str__(self):
        return f'{self.isbn}, {self.title}, {self.authorFirstName}, {self.authorLastName}, ${self.price:,.2f}' 