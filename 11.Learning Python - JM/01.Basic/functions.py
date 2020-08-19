#
# Example file for working with functions
#

# define a basic function
def func1():
    print("This is func1")

# function that takes arguments
def func2(x, y):
    print(f"This is fun2 with x: {x} , y: {y}")

# function that returns a value
def func3(x, y):
    print("This is func3")
    return x + y


# function with default value for an argument
def power(num, pwr=1):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr - 1)


#function with variable number of arguments
def addition(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


if __name__ == "__main__":
    func1()
    func2(10, 20)
    func3(10, 20)

    print(power(5))
    print(power(5, 3))

    print(addition(1,3,4,5,6))
    print(addition(100,200))
