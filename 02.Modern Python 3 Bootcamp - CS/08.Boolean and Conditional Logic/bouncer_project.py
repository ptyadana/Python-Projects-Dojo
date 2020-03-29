#ask for age
print('***** Welcome to CLUB-101 *****')
print('Before you can enter, tell me your age?')
age = input()

if age:
    age = int(age)
    if age >= 21:
        print(f'Welcome to the club! Because you are {age} years old, you are also allowed to drink. Enjoy!')
    elif age >= 18:
        print(f'Welcome to the club! As you are {age} years old, here is your wristband. You must wear this at all time during your stay in the club. Enjoy!')
    else:
        print(f'Sorry! As you are only {age} years old, you can\'t enter the club!')
else:
    print('If you don\'t say your age, I can\'t let you in.')
#18-21 wristband
#21+ drink, normal entry
#too young