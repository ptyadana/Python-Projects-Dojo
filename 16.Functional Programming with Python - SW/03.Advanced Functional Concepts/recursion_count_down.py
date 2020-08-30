def count_down(x):
    if x == 0:
        print("Done!")
        return
    print(x)
    count_down(x-1)


count_down(10)
