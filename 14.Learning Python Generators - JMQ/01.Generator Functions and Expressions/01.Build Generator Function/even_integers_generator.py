# This is generator function which will return generator object
def even_integers_function(n):
    for i in range(n):
        if i%2 == 0:
            yield i


if __name__ == "__main__":
    even_gen = even_integers_function(10)
    print(even_gen) #generator object got returned.
    print(list(even_gen)) #now generator object yeild the results