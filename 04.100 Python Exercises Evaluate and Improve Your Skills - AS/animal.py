money = int(input())
animal_price_list = {
    'chicken': 23,
    'goat': 678,
    'pig': 1296,
    'cow': 3848,
    'sheep': 6769
}

def animal_selection(animal_name, price, amount):
    animal_dict = {}
    number_of_animal = 0
    remaining_amount = 0
    if amount >= price:
        number_of_animal = amount // price
        remaining_amount = amount % price
        animal_dict = {
            'animal': animal_name,
            'number_of_animal': number_of_animal,
            'remaining_amount': remaining_amount
        }
        
    return animal_dict

animal_bought = {}

if money >= animal_price_list['sheep']:
    animal_bought = animal_selection('sheep', int(animal_price_list['sheep']), money)
elif money >= animal_price_list['cow']:
    animal_bought = animal_selection('cow', animal_price_list['cow'], money)
elif money >= animal_price_list['pig']:
    animal_bought = animal_selection('pig', animal_price_list['pig'], money)
elif money >= animal_price_list['goat']:
    animal_bought = animal_selection('goat', animal_price_list['goat'], money)
elif money >= animal_price_list['chicken']:
    animal_bought = animal_selection('chicken', animal_price_list['chicken'], money)
else:
    print('None')

if animal_bought:
    animal = animal_bought['animal']
    number_of_animal =  animal_bought['number_of_animal']
    remaining_amount = animal_bought['remaining_amount']
    if number_of_animal == 1:
        print(f'{number_of_animal} {animal}')
    elif animal == 'sheep' and number_of_animal > 1:
        print(f'{number_of_animal} {animal}')
    elif number_of_animal > 1:
        print(f'{number_of_animal} {animal}s')   
        

