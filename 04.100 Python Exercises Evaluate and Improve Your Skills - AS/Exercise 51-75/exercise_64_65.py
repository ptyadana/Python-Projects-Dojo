# The following code prints Hello, checks if 2 is greater than 1 and then breaks the loop because 2 is
# acutally greater than 1. Therefore Hi is not printed out. Please replace break with something else so that
# Hello an Hi are printed out repeatedly.

# while True:
#     print('Hello')
#     if 2 > 1:
#         break
#     print('Hi')

#Answer using continue:
while True:
    print('Hello')
    if 2 > 1:
        continue
    print('Hi')


#Answer 2 using pass:
while True:
    print('Hello')
    if 2 > 1:
        pass
    print('Hi')