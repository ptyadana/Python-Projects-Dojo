from csv import reader,writer

with open('fighters.csv') as file:
    csv_reader = reader(file)
    fighters = [[item.upper() for item in row] for row in csv_reader]
    for fighter in fighters:
        print(fighter)

with open('capatalized_fighters.csv','w', newline='') as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)