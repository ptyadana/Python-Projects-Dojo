#create a program that asks the user submit text repeatedly
#The program will exit when user submit CLOSE
#print the output as text file

with open('./96_file/96_file.txt', 'w') as file:
    while True:
        user_input = input('Enter anything (to quite- type CLOSE) : ');
        if user_input == 'CLOSE':
            break;
        else:
            file.write(user_input + '\n');