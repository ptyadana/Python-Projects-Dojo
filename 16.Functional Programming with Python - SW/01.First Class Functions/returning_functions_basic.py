def create_printer():
    def printer():
        print("Hello functional!")
    return printer


my_printer = create_printer()
my_printer()
