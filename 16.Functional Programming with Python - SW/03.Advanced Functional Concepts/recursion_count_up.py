def count_up(x, maximum):
    if x > maximum:
        print("Done!")
        return
    print(x)
    count_up(x+1, maximum)


count_up(1, 10)
