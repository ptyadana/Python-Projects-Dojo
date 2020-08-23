# Python Logical Operators: And, Or, Not:

# What is a Boolean?
isRaining = False
isSunny = True

# Logical Operators -> Special Operators for Booleans

# AND
# true and true --> true
# false and true --> false
# true and false --> false
# false and false --> false
if isRaining and isSunny:
    print("Rainbow might appear")


# OR
# true and true --> true
# false and true --> true
# true and false --> true
# false and false --> false
if isRaining or isSunny:
    print("It's might be raining or sunny.")

# NOT
# true --> false
# false --> true
if not isRaining:
    print("Raining")

ages = [19, 12, 4, 18, 21, 6]
for age in ages:
    is_adult = age > 17
    if not is_adult:
        print(f"being {age} doesn't make you an adult")
