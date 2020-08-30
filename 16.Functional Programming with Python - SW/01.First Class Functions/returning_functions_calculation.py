
# As we can see double, triple and quadruple are essentially doing very same operations
# so there much be a better way of doing those.
# def double(x):
#     return x * 2


# def triple(x):
#     return x * 3


# def quadruple(x):
#     return x * 4


# -------------------------
# Using Creator Function
def create_multiplier(multipier_num):
    def multipler(x):
        return x * multipier_num

    return multipler


# usage
double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(5))
print(triple(5))
print(quadruple(5))
