# Create a program that asks the user to input values separated by commas 
# and stores those values in a text file, each value in a separate line.

data = input('Please enter any value seperated with , comma : ').split(',');
print(data)
with open('./95_file/95_file.txt', 'w') as file:
    for value in data:
        file.write(value+'\n');
