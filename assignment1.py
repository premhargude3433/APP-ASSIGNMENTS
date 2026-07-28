class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
        self.borrowed = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"{book} added successfully.")

    def register_patron(self, patron):
        self.patrons.append(patron)
        print(f"{patron} registered successfully.")

    def borrow_book(self, patron, book):
        if patron not in self.patrons:
            print("Patron not registered.")
        elif book not in self.books:
            print("Book not available.")
        else:
            self.books.remove(book)
            self.borrowed[book] = patron
            print(f"{patron} borrowed '{book}'.")

    def return_book(self, book):
        if book in self.borrowed:
            patron = self.borrowed.pop(book)
            self.books.append(book)
            print(f"{patron} returned '{book}'.")
        else:
            print("Book was not borrowed.")

    def display_info(self):
        print("\nAvailable Books:", self.books)
        print("Registered Patrons:", self.patrons)
        print("Borrowed Books:", self.borrowed)


library = Library()

library.add_book("Python Programming")
library.add_book("Data Structures")
library.add_book("Machine Learning")

library.register_patron("Alice")
library.register_patron("Bob")

library.borrow_book("Alice", "Python Programming")

library.return_book("Python Programming")

library.display_info()