r = range(0, 30)
print(type(r))
print(type(10))
print(type("A"))
print(type("DKKSDL"))


class Car:
    pass

class Truck(Car):
    pass

c = Car()
convert = Car()
t = Truck()
print(type(c))
print(type(t))

print(type(c) == type(t))
print(type(c) == type(convert))

print(isinstance(c, Car))
print(isinstance(t, Truck))


if isinstance(r, range):
    print(list(r))