# Question: Create a script that generates a file where all letters of English alphabet 
# are listed two in each line. The inside of the text file would look like:

# ab
# cd
# ef

# and so on.


# Answer 1 (cleaner one):
import string
with open('output_43.txt','w') as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
        file.write(letter1 + letter2 + '\n')

# Answer 2:
index = 0
for i in range(len(string.ascii_lowercase)//2):
    print(string.ascii_lowercase[index:index+1], string.ascii_lowercase[index+1:index+2])
    index += 2
