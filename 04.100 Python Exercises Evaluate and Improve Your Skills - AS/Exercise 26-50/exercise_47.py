#Write a script that iterates through each of the 26 tex files. checks if the letter insides the text file
# is in string "python" and puts the letters in the list if the letter is a character of "python"

# Hint: Like the previous exercise, but here you need to add a conditional inside the loop


#Answer:
import glob

file_list = glob.glob('output_45/[a-z].txt')
letter_list = []
checkword = 'python'

for filename in file_list:
    with open(filename,'r')as file:
        letter = file.read()
    if letter in checkword:
        letter_list.append(letter)

print(letter_list)
