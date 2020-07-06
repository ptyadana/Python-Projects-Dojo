#create a program that asks the user submit text repeatedly
#The program saves the changes when user submit SAVE, but doesn't close
#The programe saves the changes and exit when user submit CLOSE
#print the output as text file

data_list = []

with open('97_file/97_file.txt', 'w') as file:
    while True:
        user_input = input('Enter anything (to save - type SAVE, to quite- type CLOSE) : ');
        if user_input == 'CLOSE':
            break;
        elif user_input != 'SAVE':
            data_list.append(user_input);
        elif user_input == 'SAVE':
            for data in data_list:
                file.write(data + '\n');
