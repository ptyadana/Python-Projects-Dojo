import random

health = 100
difficulty = 1
enemy = {'1':'Goblin', '2':'Troll', '3':'Orge'}

def face_enemy(current_health):
    attack_level = random.randint(1,3)   
    current_health = current_health - (attack_level * 20)

    player_status = {
        'current_health' : current_health, 
        'enemy_type' : enemy[str(attack_level)],
    }

    return player_status

def adventure():
    global health
    print('***** Welcome to Endless Forest Adventure *****')
    print('to quit at anytime type - quit\n')

    while True:
        print(f'\nYour current health: {health}')
        user_input = input('to continue to walk.. press Enter')

        if user_input == 'quit':
            break
        elif health <= 0:
            print('\nYou have no more health left and you fell down! Game Over! Thanks for Playing :)')
            break
        else:
            random_luck = random.randint(1, 2)

            if random_luck == 1:
                player_status = face_enemy(health)
                enemy_type = player_status ['enemy_type']
                health = player_status['current_health']

                print(f'\nYou heard something approaching to you. There was {enemy_type} attacking you.')
                print(f'You fought it back. You lost some health.')
            else:
                print('\nYou found Magic Portion and You drank it.')
                portion_health = random.randint(25, 50) // difficulty
                health += portion_health

if __name__ == "__main__":
    adventure()
