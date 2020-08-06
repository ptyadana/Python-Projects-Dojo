items = ["list", "of", "words"]

def count_letters(x):
    return len(x)

new_items = list(map(count_letters, items))
print(new_items)