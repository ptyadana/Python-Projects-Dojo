flims = {
    'Toy Story': [3, 5],
    'Mission Impossible': [10, 6],
    'Wonder Woman': [3, 2],
    'Deadpool': [18, 4],
    'Mad Max Fury': [16, 7]
}

print('\n***** Welcome to Awesome Cinema *****')
print('----- Today Movies ----- ')
for f in flims.keys():
    print(f)

while True:
    choice = input('\nHi.. Which flim would like to watch? : ').strip().title()

    if choice in flims:
        age = int(input('How old are you? : ').strip())

        if age >= flims[choice][0]:
            avaliable_seats = flims[choice][1]
            if avaliable_seats > 0:
                flims[choice][1] = avaliable_seats - 1
                print('\nEnjoy the flim :)')
            else:
                print('\nI am sorry. We are sold out.')
        else:
            print('\nI am sorry. You are not old enough to watch that flim yet.')
    else:
        print('I am sorry. We do not show that flim.')

