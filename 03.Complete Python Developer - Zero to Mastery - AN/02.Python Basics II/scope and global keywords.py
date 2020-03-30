#Scope : how python refer the scope in order
#1) - start with local
#2) - parent local?
#3) - global variable?
#4) - python built in function
total = 0

def count():
    global total
    total += 1
    return total


count()
count()
print(count())