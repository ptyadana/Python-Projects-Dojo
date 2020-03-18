from csv import DictReader

#reading file with specific delimiter
with open('fighters_with_pipe.csv') as file:
    csv_dict_reader = DictReader(file,delimiter='|')

    for row in csv_dict_reader:
        print(row)