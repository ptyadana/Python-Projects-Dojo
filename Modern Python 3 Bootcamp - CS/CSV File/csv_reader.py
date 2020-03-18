from csv import reader

with open('fighters.csv') as file:
    csv_reader = reader(file)

    #to avoid getting the first line => Name is from Country
    next(csv_reader)
    
    for fighter in csv_reader:
        #each row is a list
        print(f'{fighter[0]} is from {fighter[1]}')