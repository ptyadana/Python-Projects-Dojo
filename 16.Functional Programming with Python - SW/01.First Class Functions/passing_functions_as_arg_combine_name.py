def combine_name(func):
    return func("John", "Doe")


def append_with_space(st1, st2):
    return f"{st1} {st2}"


def get_government_form_noation(first, last):
    return f"{last.upper()}, {first.upper()}"


# testing
result = combine_name(append_with_space)
print(result)

print(combine_name(get_government_form_noation))
