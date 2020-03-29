"""
Naturally Falsy include: empty objects, empty strings, None, zero 0
"""
print('What is your favourite book?')
book = input()

if book:
    print(f'Well.. {book} is my favourite book too.')
else:
    print('I don\'t understand.')