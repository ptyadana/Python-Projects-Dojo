# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "A"

class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "B"


class C(B,A):
    def __init__(self):
        super().__init__()
    
    def show_properties(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
c.show_properties()

# Python has Method Resolution Order
# if we change the order of the inheritance definition, it will change.
print(C.__mro__)