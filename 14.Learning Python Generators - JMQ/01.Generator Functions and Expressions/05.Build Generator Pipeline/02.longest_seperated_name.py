# use generators to find out the longest name
# add another seperate_names generator as another stage in pipeline

def seperate_names(names):
    for full_name in names:
        for name in full_name.split(" "):
            yield name # first name and last name seperately
            

full_names = (name.strip() for name in open("names.txt"))
names = seperate_names(full_names)
lengths = ((name, len(name)) for name in full_names)
longest = max(lengths, key=lambda x: x[1])

print(list(longest))