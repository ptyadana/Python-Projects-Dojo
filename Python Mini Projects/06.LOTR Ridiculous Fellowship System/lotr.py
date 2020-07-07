members = ['Frodo', 'Merry', 'Sam', 'Pippin', 'Aragorn', 'Boromir', 'Legolas', 'Gimli', 'Gandalf']

print('***** Welcome to Ridiculous Fellowhip System *****')

while True:
    print('\nHello, My name is Radi.')
    name = input('Please state your name? ').strip().capitalize()

    if name in members:
        print(f'\nWelcome back! {name}')
        choice = input(f'You are part of the followship. Would you like to remain? (Y/N): ')
        
        if choice.capitalize() == 'N':
            members.remove(name)
            print('\nOh.. it is a shame to let you go.')
            print(f'Next please...')
    else:
        choice = input(f'\nI do not recogize you {name}. Would you like to join the fellowship? (Y/N): ')
        
        if choice.capitalize() == 'Y':
            members.append(name)
            print(f'\nIt is good to have you {name}.')
            print(f'Next please...')
        else:
            print('\nOh.. I do hope you do not regret your choice sire..')
            break

count = len(members)
print(f'\n---- here are {count} Brave and Courage souls of LOTR fellowship ----')
for member in members:
    print(member)