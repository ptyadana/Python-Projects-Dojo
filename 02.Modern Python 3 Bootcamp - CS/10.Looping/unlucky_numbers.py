"""
for 4 and 13, unlucky
for even numbers, even
for ood numbers, odd
"""

for num in range(21):
    if num == 4 or num == 13:
        print(f"{num} is UNLUCKY!")
    elif num%2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")