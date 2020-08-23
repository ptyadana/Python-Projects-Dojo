# Python Comparison Operators

# TIPS:
# == --> is equal to
# <= --> is less than or equal to
# >= --> is greater than or equal to
# < --> is less than
# > --> is greater than



# < --> is less than
print(10 > 15)
print(15 > 9)

# == --> is equal to
print(9 == 9)
print(8 == 10)

# < --> is less than
mouse = 1
kitten = 9
tiger = 65
if mouse < kitten and mouse < tiger:
    print("mouse weights the least.")

#False --> 0
#True --> 1
# > --> is greater than
print(False > True)

# Looking for first mismatched letter
# A - Z --> 1 - 26
# > --> is greater than
print("Jennifier" > "Jenny") #this case, python looks for first mismatched letter, "i" vs "y"

# A - Z --> 1 - 26
# <= --> is less than or equal to
print("a" <= "b")