def say_hello(name):
    print(f"Hello {name}")


if __name__ == "__main__":
    say_hello2 = say_hello
    say_hello2("John")
