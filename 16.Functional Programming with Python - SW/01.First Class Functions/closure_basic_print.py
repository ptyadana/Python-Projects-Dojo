def create_printer():
    my_favourite_number = 123

    def printer():
        print(f"My Favourite Number is {my_favourite_number}")
    return printer


# Closure
# As we can see, the output will be 123. Which means my_printer can still access to my_favourite_number which is outer scope.
# this is what Closure is
my_printer = create_printer()
my_printer()
