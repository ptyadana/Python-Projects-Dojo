# similar to partial application, but only with one level deeper

def curry_add(x):
    def curry_add_inner(y):
        def curry_add_inner_2(z):
            return x + y + z
        return curry_add_inner_2
    return curry_add_inner


add_5 = curry_add(5)
add_5_and_6 = add_5(6)
print(add_5_and_6(7))

# or we can even call like below
print(curry_add(5)(6)(7))
