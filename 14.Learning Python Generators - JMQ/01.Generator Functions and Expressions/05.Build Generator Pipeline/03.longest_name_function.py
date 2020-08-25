def seperate_names(names):
    for full_name in names:
        for name in full_name.split(" "):
            yield name # first name and last name seperately
            

def get_longest(name_list_file):
    full_names = (name.strip() for name in open(name_list_file))
    names = seperate_names(full_names)
    lengths = ((name, len(name)) for name in full_names)
    return max(lengths, key=lambda x: x[1])

if __name__ == "__main__":
    result = get_longest("names.txt")
    print(result)
