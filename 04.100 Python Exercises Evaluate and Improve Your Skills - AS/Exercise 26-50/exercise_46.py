#Write a script that extracts letters from the 26 text files
#and put the letters in a list

# Hint: Use glob.glob to create a list of file paths and then iterate through 
# that list reading the content of each file.

#Answer:
import glob

file_list = glob.glob('output_45/[a-z].txt')
letter_list = []

for filename in file_list:
    with open(filename,'r')as file:
        letter_list.append(file.read())

print(letter_list)
