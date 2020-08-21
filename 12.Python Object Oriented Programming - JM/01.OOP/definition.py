# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


#  create a basic class
class Book():
    def __init__(self, title):
        self.title = title

#  create instances of the class
b1 = Book("Flip it!")
b2 = Book("Positive Dog")

#  print the class and property
print(b1)
print(b1.title)