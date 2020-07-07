import random

print('***** Welcome to Baby Conversation Simulator *****')

questions = {
    '1': 'Why is the sky blue?',
    '2': 'What does God look like?',
    '3': 'Where do you go when you die?',
    '4': 'Why is water wet?',
    '5': 'Where do babies come from?',
}

number = random.randint(1,5)

answer = input(f'\n{questions[str(number)]} : ')
while answer != 'just because':
    answer = input('Why?').strip().lower()

print('oh... ok')