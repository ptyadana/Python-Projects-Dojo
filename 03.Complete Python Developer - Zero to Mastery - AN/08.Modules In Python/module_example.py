print(__name__)

import module_utilities
# from shopping import shopping_cart
from shopping.shopping_cart import buy

if __name__ == "__main__":
    print(module_utilities.multiply(10,2))
    print(module_utilities.divide(100,2))

    # print(shopping_cart.buy("apple"))

    #cleaner version
    print(buy("apple"))