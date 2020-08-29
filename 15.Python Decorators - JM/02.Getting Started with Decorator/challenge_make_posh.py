def make_posh(func):
    def wrapper():
        length = len("Fibonacci")

        print("+" + "-" * length + "+")
        print("|" + " " * length + "|")
        result = func()
        print(result)
        print("|" + " " * length + "|")
        print("+" + "=" * length + "+")
        return result

    return wrapper


@make_posh
def pfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '


if __name__ == "__main__":
    print(pfib())
