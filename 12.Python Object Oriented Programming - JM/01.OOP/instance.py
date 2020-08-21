# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title):
        self.title = title
        #  add properties

    #  create instance methods


#  create some book instances
b1 = Book("War and Peace")
b2 = Book("The Catcher in the Rye")

#  print the price of book1


#  try setting the discount


#  properties with double underscores are hidden by the interpreter
