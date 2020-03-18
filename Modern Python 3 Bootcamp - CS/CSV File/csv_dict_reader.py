from csv import DictReader

with open('fighters.csv') as file:
    csv_dict_reader = DictReader(file)

    for row in csv_dict_reader:
        print(row)
        print(row['Name'])