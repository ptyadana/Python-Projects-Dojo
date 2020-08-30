def create_counter():
    count = 0

    def get_count():
        return f"Current Count: {count}"

    def increment():
        nonlocal count
        count += 1

    return (get_count, increment)


# Closure Usage
get_count, increment = create_counter()
print(get_count())
increment()
increment()
print(get_count())
increment()
increment()
increment()
print(get_count())
