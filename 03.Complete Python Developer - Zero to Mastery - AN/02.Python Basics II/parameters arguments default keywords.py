#parameters
# def hello(name, emoji):
#     print(f"hello {name} {emoji}")

#keyword parameters
def hello(name="Luke Skywalker", emoji="<3"):
    print(f"hello {name} {emoji}")

#arguments
#positional arguments
#follow the correct orders
hello("Richard", ":)")
hello("Vivian", ":D")

#keywords arguments
#not best pratice
hello(emoji=":P", name="Kid")

hello()
hello("Babe")