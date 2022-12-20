# Catalog.py
# This program processes a menu system which allows user to select different options to play with the system. 
# Author: Yanan Wu
# Date: 26/11/2022

from Book import Book
import tkinter as Tk
from tkinter.simpledialog import askfloat, askstring, askinteger
from tkinter import * 
from tkinter import messagebox

class Catalog:
    def __init__(self, books):
        self.books = books

    def addBook(self, book):
        self.books.append(book)

    def sortByPrice(self):
        self.books.sort(key=lambda x: x.price, reverse = False)

    def searchByTitle(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book

    def deleteBook(self, isbn):
        for book in self.books:
            if isbn.lower() == book.isbn.lower():
                choice = messagebox.askyesno(message=str(book)+'\n\n'+'Are you sure you want to delete this book?')
                if choice: 
                    self.books.remove(book)
                    return True
                else:
                    return False
        return False

    def displayBooks(self):
        message = ''
        for book in self.books:
            message += str(book) + "\n\n"       
        if len(message) == 0:
            showMessageDialog('There are no books in the catalog')
        showMessageDialog(message)

# print option menu system message box
message = '''
--Homesglen Book Store --

1. Add a book
2. Sort and display by price
3. Search for a book by title
4. Delete a book
5. Display all books
6. Exit

Enter menu choice:
'''

# create a list of default books
defaultBooks = [Book('0553296981', 'The Diary of a Young Girl', 'Frank', 'Anne', 16.5), Book('1400082773', 'Dreams from My Father', 'Obama', 'Barrack', 24.99 ), Book('1323400083', 'Principles', 'Ray', 'Dalio', 19.99)]
catalog = Catalog(defaultBooks)

# method to show the message box
def showMessageDialog(message):
    messagebox.showinfo(message = message)

# method to get book information
def askBookInfo():
    isbn = askstring('Book Catalog', 'Enter ISBN:')
    if isbn == '' or isbn is None or isbn.isnumeric() != True:
        showMessageDialog("Please enter a valid ISBN!")
        return
    title = askstring('Book Catalog', 'Enter title:')
    if title == '' or title is None:
        showMessageDialog('Please enter a valid title!')
        return
    authorFirstName = askstring('Book Catalog', 'Enter author first name:')
    if authorFirstName == '' or authorFirstName is None or authorFirstName.isnumeric():
        showMessageDialog('Please enter a valid author first name!')
        return
    authorLastName = askstring('Book Catalog', 'Enter author last name:')
    if authorLastName == '' or authorLastName is None or authorLastName.isnumeric():
        showMessageDialog('Please enter a valid author last name!')
        return
    price = askfloat('Book Catalog', 'Enter price:')
    if price == '' or price is None:
        showMessageDialog('Please enter a valid price!')
        return

    return Book(isbn=isbn, title=title, authorFirstName=authorLastName, authorLastName=authorLastName, price=price)

window = Tk()
window.wm_withdraw()
shouldExitProgram = False
while shouldExitProgram == False:
    option = askinteger('Book Catalog', message)
    if option == 1:
        book = askBookInfo()
        catalog.addBook(book)
    elif option == 2:
        catalog.sortByPrice()
        catalog.displayBooks()
    elif option == 3:
        title = askstring('Book Catalog', 'Enter title to search:')
        if title == '' or title is None:
            showMessageDialog('Please enter a valid title!')
            continue
        else:
            book = catalog.searchByTitle(title)
            if book:
                showMessageDialog(str(book))
            else:
                showMessageDialog('Book not found')
    elif option == 4:
        isbn = askstring('Book Catalog', 'Enter ISBN:')
        if isbn == '' or isbn is None or isbn.isnumeric() != True:
            showMessageDialog('Please enter a valid ISBN!')
            continue
        isDeleted = catalog.deleteBook(isbn)
        if isDeleted:
            showMessageDialog('Book HAS been deleted')
        else: 
            showMessageDialog('Book has NOT been deleted')
    elif option == 5:
        catalog.displayBooks()
    elif option == 6:
            choice = messagebox.askyesno(message = 'Are you sure you want to exit?')
            if choice == True:
                shouldExitProgram = True
    else:
        showMessageDialog('Please enter a valid option or enter 6 to exit the program')
        shouldExitProgram = False

window.withdraw()

