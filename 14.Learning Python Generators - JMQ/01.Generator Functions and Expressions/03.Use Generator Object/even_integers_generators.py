# This is generator function which will return generator object
def even_integers_function(n):
    for i in range(n):
        if i%2 == 0:
            yield i


if __name__ == "__main__":
    even_gen = even_integers_function(10)
    
    print(even_gen.__next__())
    print(even_gen.__next__())
    print(even_gen.__next__())
    print(even_gen.__next__())
    print(even_gen.__next__())
    # print(even_gen.__next__()) # call again for next item will cause StopIteration error.

    # if we use for loop, python for loop will handle it.
    # but there won't be no result, because the generator is exhausted and no item to return.
    for item in even_gen:
        print(item)
    # but we can create a new generator object and call it again to get the results.

