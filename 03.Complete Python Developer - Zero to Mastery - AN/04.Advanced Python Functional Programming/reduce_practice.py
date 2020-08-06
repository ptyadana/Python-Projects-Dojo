from functools import reduce

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item # acc gets assign this result on next run

# items = [1, 2, 3]

# print("Result: ", reduce(accumulator, items, 10))


#reducing list of string into total word length
def word_length(acc, item):
    # return len(item) + acc
    return {item: len(item)}

items = ["list", "of", "words"]

print("Total Length: ", reduce(word_length, items, 0))