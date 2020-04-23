# Question: Please create a script that generates 26 text files named a.txt, b.txt, 
# and so on up to z.txt. Each file should contain a letter reflecting its filename. 
# So, a.txt will contain letter a, b.txt will contain letter b and so on.

# Answer:

import string

def create_file_by_letter(letter):
    with open('./output_45/'+letter+'.txt','w') as file:
        file.write(letter)

def files_for_each_alphabets():
    for letter in string.ascii_lowercase:
        create_file_by_letter(letter)

if __name__ == "__main__":
    files_for_each_alphabets()
