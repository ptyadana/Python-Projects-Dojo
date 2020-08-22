# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects

from dataclasses import dataclass
#data classes are available for python 3.7 or later

@dataclass
class Book:
    title : str
    author : str
    pages : int
    price : float

    def book_info(self):
        return f"{self.title} by {self.author}"

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)

# print the book itself - dataclasses implement __repr__
# dataclass automatically creat __repr__
print(b1)

# comparing two dataclasses - they implement __eq__
print(b1 == b3)
print(b1 == b2)

# TODO: change some fields
b3.author = "JK.Rowling"
b3.title = "Harry Potter"
print(b3.book_info())