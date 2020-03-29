a = [1,2,3]
b = [1,2,3]
c = b

#contents of a and b are equal
if a == b:
    print('a == b')


#a and b are different instances
if a is b:
    print('a is b')

if c is b:
    print('c is b')