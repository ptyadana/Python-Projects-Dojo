# Question: Create an English to Portuguese translation program.

# The program takes a word from the user as input and translates it using the following dictionary as 
# a vocabulary source. In addition, return the message "We couldn't find that word!" 
# when the user enters a word that is not in the dictionary. 
# Also, make the program non case-sensitive meaning that for example, both earth and Earth should 
# return the translation correctly for that word.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Expected output: 
# Enter word: hello
# We couldn't find that word!

# Answer:
def vocab(word):
    try:
        return d[word.lower()]
    except KeyError:
        return 'We couldn\'t find that word!'
    

user_input = input('Enter word: ')
print(vocab(user_input))

# Explanation:
# As you see we are converting all the characters of the string to lowercase as soon as we receive the input from the user. Then we simply pass the lowercase version of the string to the dictionary.