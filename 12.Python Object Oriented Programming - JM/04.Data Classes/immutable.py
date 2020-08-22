# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self, newvalue):
        self.value2 = newvalue

obj = ImmutableClass()
print(obj.value1)
print(obj)

# attempting to change the value of an immutable class throws an exception
obj.value1 = "Some other value"
print(obj.value1)

# even functions within the class can't change anything
obj.somefunc(50)
print(obj)