def pfib(*args, **kwargs):
    print(args)
    print(kwargs)


def wrapper(*args, **kwargs):
    print("In wrapper function.")
    print(*args)
    pfib(*args, **kwargs)


if __name__ == "__main__":
    wrapper(1, 1, th=2)
